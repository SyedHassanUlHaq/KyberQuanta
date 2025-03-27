`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/15/2024 03:49:25 PM
// Design Name: 
// Module Name: Sha3_256
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Sha3_512#(
    parameter DATAIN = 2320,
    parameter RATE = 576
)
(
    input logic clk,
    input logic rst,
    input logic [DATAIN - 1 :0] datain,
    output logic [0:511] digest
);
    
    logic chk;
    logic [63:0] A_temp [0:4][0:4];
    
    logic [1599:0] X_temp;
    logic [1599:0] state_temp;
    logic [RATE-1 :0] datain_temp;
    logic [3:0] round_count,mul_count;
    logic [3:0] idle_count;
    logic r_done;
    logic r_start;
    
    logic [RATE-1:0] aa,bb,cc,dd;
   
    typedef enum logic [1 : 0] {
        IDLE,
        Process_Block, Padding, Finall
    } state_type;
    
    state_type state, next_state;
    
//    always_ff @(posedge clk or posedge rst) begin
//                if (rst) begin
//                    state <= IDLE;
//                    mul_count <= 4'b0;
//                    round_count <= 4'b0;
//                    digest <= 256'b0;
//                end
//                else begin
//                    if (r_done == 1'b1) begin
//                        mul_count = mul_count + 1;
//                        round_count = round_count + 1;
//                    end
//                    state <= next_state;
                    
//                end
//            end

    logic [0:511] digest_reg;

// Always_ff block for synchronous updates
always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
        state <= IDLE;
        mul_count <= 4'b0;
        round_count <= 4'b0;
        digest_reg <= 256'b0;  // Clear digest_reg on reset
    end
    else begin
        if (r_done == 1'b1) begin
            mul_count <= mul_count + 1;
            round_count <= round_count + 1;
        end

        state <= next_state;

        if (state == Padding && r_done == 1'b1) begin
            digest_reg <= {X_temp[7:0], X_temp[15:8], X_temp[23:16], X_temp[31:24], 
         X_temp[39:32], X_temp[47:40], X_temp[55:48], X_temp[63:56], 
         X_temp[71:64], X_temp[79:72], X_temp[87:80], X_temp[95:88], 
         X_temp[103:96], X_temp[111:104], X_temp[119:112], X_temp[127:120], 
         X_temp[135:128], X_temp[143:136], X_temp[151:144], X_temp[159:152], 
         X_temp[167:160], X_temp[175:168], X_temp[183:176], X_temp[191:184], 
         X_temp[199:192], X_temp[207:200], X_temp[215:208], X_temp[223:216], 
         X_temp[231:224], X_temp[239:232], X_temp[247:240], X_temp[255:248], 
         X_temp[263:256], X_temp[271:264], X_temp[279:272], X_temp[287:280], 
         X_temp[295:288], X_temp[303:296], X_temp[311:304], X_temp[319:312], 
         X_temp[327:320], X_temp[335:328], X_temp[343:336], X_temp[351:344], 
         X_temp[359:352], X_temp[367:360], X_temp[375:368], X_temp[383:376], 
         X_temp[391:384], X_temp[399:392], X_temp[407:400], X_temp[415:408], 
         X_temp[423:416], X_temp[431:424], X_temp[439:432], X_temp[447:440], 
         X_temp[455:448], X_temp[463:456], X_temp[471:464], X_temp[479:472], 
         X_temp[487:480], X_temp[495:488], X_temp[503:496], X_temp[511:504]};
          end
    end
end
      
    always_comb begin
//        aa=datain[1087:0];
//        bb=datain[2175:1088];
//        cc=datain[3263:2176];
//        dd=datain[3999:3264];
        next_state = state;
        if (DATAIN > RATE) begin
            chk = 1'b0;
            datain_temp = datain[RATE-1:0];
            state_temp = 1600'b0;
            r_start = 1'b0;
            case(state)
                IDLE: begin
                r_start = 1'b1;
                    if (r_done == 1'b0) begin
                        
                        next_state = IDLE;
                    end
                    else begin
                        if (DATAIN/RATE==1'b1) begin 
                        
                            next_state = Padding;
                        end 
                        else begin
                            next_state = Process_Block;
                        end
                    end                  
                end

                   Process_Block: begin
                    r_start = 1'b1;
                    if (r_done == 1'b0) begin
                            chk=1'b0;
                            state_temp = X_temp;
                            datain_temp = datain >> ((mul_count)*RATE);
                            next_state = Process_Block;
                    end
                    else begin
                        if (round_count < {DATAIN / RATE}-1) begin
                            next_state = Process_Block;
                        end else begin
                            next_state = Padding;
                        end
                    end                                                   
                end
                
                Padding: begin
                    r_start = 1'b1;
                    chk=1'b1;
                    state_temp = X_temp;
                    datain_temp = datain >> ((mul_count)*RATE);
                    if (r_done == 1'b0) begin
                        
                        next_state = Padding;
                    end
                    else begin
                        next_state = Finall;
                    end
                    
                      
                end
                
                Finall: begin
//                    digest = digest_reg;
                     next_state = Finall;
                end
                
            endcase
        end
        else begin
            
            chk = 1'b1;
            r_start = 1'b1;
            datain_temp = datain;
            state_temp = 1600'b0;
//            state = Padding;
            case (state)
                IDLE: begin
                    next_state = Padding;
                end

                Padding: begin
                    chk = 1'b1;       // Enable padding
                    r_start = 1'b1;   // Start padding round
                    if (r_done == 1'b1) begin
                        next_state = Finall;
                    end
                    else begin
                        next_state = Padding;
                    end
                end

                Finall: begin
                    r_start = 1'b0;
                    next_state = Finall;
                    
                end
            endcase


        end 
     end    
    padding u_padding (
        .check(chk),
        .datain(datain_temp),
        .state(state_temp),
        .A(A_temp)
    );
    
    fn_top u_fn_top (
        .clk(clk),
        .rst(rst),
        .round_start(r_start),
        .A(A_temp),
        .X(X_temp),
        .round_done(r_done)
    );
    
    assign digest = digest_reg;

endmodule