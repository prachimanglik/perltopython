// Generating Go2UVM Test for WaveDrom file: {vw_wd_fname}
// ---------------------------------------------------------
// Automatically generated from VerifWorks's DVCreate-Go2UVM product
// Thanks for using VerifWorks products, see http://www.verifworks.com for more
import uvm_pkg::*;
`include "vw_go2uvm_macros.svh"
// Import Go2UVM Package 
import vw_go2uvm_pkg::*;
// Use the base class provided by the vw_go2uvm_pkg
`G2U_TEST_BEGIN( vw_wd_g2u_test) 
  // Create a handle to the actual interface
  virtual vw_wd_g2u_if vif; 

  function void build_phase(uvm_phase phase); 
    if (!uvm_config_db#(virtual vw_wd_g2u_if)::get( 
      .cntxt(null), .inst_name("*"), 
      .field_name("vif"), .value(vif))) begin : no_vif
        `g2u_fatal("Unable to connect virtual interface to physical interface, check uvm_config_db::set in top module") 
    end : no_vif 
    else begin : vif_connected 
      `g2u_display("Successfully hooked up virtual interface") 
    end : vif_connected 
  endfunction : build_phase 

  task reset;
    `g2u_display (log_id, "Start of reset", UVM_MEDIUM)
    `g2u_display (log_id, "Fill in your reset logic here ", UVM_MEDIUM)
    // this.vif.cb.rst_n <= 1'b0;
    // repeat (5) @ (this.vif.cb);
    // this.vif.cb.rst_n <= 1'b1;
    // repeat (1) @ (this.vif.cb);
    `g2u_display (log_id, "End of reset", UVM_MEDIUM)
  endtask : reset
  task drive_vlb_wr_rd; 
    `g2u_display("Driving signal: vlb_wr_rd") 
    vif.vlb_wr_rd <= P......;
    @(vif.cb);
  task drive_vlb_wr_rd_valid; 
    `g2u_display("Driving signal: vlb_wr_rd_valid") 
    vif.vlb_wr_rd_valid <= P......;
    @(vif.cb);
    `g2u_display("End of stimulus for signal: vlb_wr_rd_valid") 
  endtask : drive_vlb_wr_rd_valid 

  task main ();
    `g2u_display (log_id, "Start of main", UVM_MEDIUM)
    fork 
     drive_vlb_wr_rd; 
     drive_vlb_wr_rd_valid; 
    join 
    // this.vif.cb.inp_1 <= 1'b0;
    // this.vif.cb.inp_2 <= 22;
    // repeat (5) @ (this.vif.cb);
    `g2u_display (log_id, "End of main", UVM_MEDIUM)
  endtask : main
`G2U_TEST_END 
