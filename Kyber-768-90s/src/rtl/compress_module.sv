module compress_module (
    input logic [31:0] x,    
    input logic [31:0] d,      
    output logic [31:0] result    
);
    localparam int q = 3329;   

    always_comb begin
        logic [31:0] t;          
        logic [31:0] y;           
        t = 1 << d;  
        y = (t * x + (q >> 1)) / q; 
        result = y % t;  
    end
endmodule