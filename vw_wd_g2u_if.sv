import uvm_pkg::* ;
import vw_go2uvm_pkg::* ;
`include "uvm_macros.svh"
`include "vw_go2uvm_macros.svh"
interface vw_wd_g2u_if();
  logic clk; 
  logic vlb_wr_rd;
  default clocking cb @ (posedge clk);
  logic vlb_wr_rd_valid;
  default clocking cb @ (posedge clk);
    output vlb_wr_rd;
   endclocking : cb 
endinterface : vw_wd_g2u_if
    output vlb_wr_rd_valid;
   endclocking : cb 
endinterface : vw_wd_g2u_if
