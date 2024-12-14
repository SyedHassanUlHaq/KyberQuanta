`timescale 1ns / 1ps

module bits_to_bytes #(
    parameter BIT_LENGTH = 2048, 
    parameter BYTE_LENGTH = BIT_LENGTH / 8
) (
    input  logic [BIT_LENGTH-1:0] bit_array,
    output logic [7:0] byte_array [BYTE_LENGTH-1:0]  // Unpacked array of bytes
);

    integer i, j;

    always_comb begin
        // Loop to assign bits to bytes in little-endian format
        for (i = 0; i < BYTE_LENGTH; i = i + 1) begin
            byte_array[i] = 8'b0; // Initialize each byte to zero
            for (j = 0; j < 8; j = j + 1) begin
                // Reverse the bits within each byte
                byte_array[i][j] = bit_array[i * 8  +( 7-j )];
            end
        end
    end

endmodule