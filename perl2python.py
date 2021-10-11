# Copyright (c) 2004-2017 VerifWorks, Bangalore, India
# http://www.verifworks.com 
# Contact: support@verifworks.com 
# 
# This program is part of Go2UVM at www.go2uvm.org
# Some portions of Go2UVM are free software.
# You can redistribute it and/or modify  
# it under the terms of the GNU Lesser General Public License as   
# published by the Free Software Foundation, version 3.
#
# VerifWorks reserves the right to obfuscate part or full of the code
# at any point in time. 
# We also support a comemrical licensing option for an enhanced version
# of Go2UVM, please contact us via support@verifworks.com
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# Lesser General Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses
from numpy import unique
vw_wd_fname = "waves.wd"
vw_wd_f = ""
wd_file_contents =""
top_mod = "vw_wd_g2u"
vw_sv_if_name = top_mod + "_if"
vw_sv_if_fname = vw_sv_if_name + ".sv"
vw_sv_if_f = ""
vw_test_name = top_mod +"_test"
vw_test_fname = vw_test_name + ".sv"
vw_test_f = ""
vw_top_name = top_mod +"_top"
vw_top_fname = vw_top_name + ".sv"
vw_top_f = " "
# BIG Assumption - clock is named "clk"
# Enhance it later
vw_clk_sig_name = "clk"

vw_flist_name = "go2uvm"
vw_flist_fname = vw_flist_name + ".f"
vw_flist_f = ""

vw_make_name = "Makefile"
vw_make_fname = vw_make_name
vw_make_f=""
try:
  vw_wd_f = open(vw_wd_fname,"r")
except Exception as E:
  print("Undable to open the file-vw_wd_fname for reading", E)


vw_flist_f = open (vw_flist_fname,"w")
vw_make_f  = open (vw_make_fname,"w")


# Read all content in a single variable
# Override carriage return for this file read alone
wd_file_contents = vw_wd_f.read()
print("File contents ..")
print(wd_file_contents)
#Restore for normal behaviour later in script
try:
  vw_sv_if_f = open(vw_sv_if_fname,"w")
except Exception as E:
  print("Undable to open the file-vw_sv_if_fname for writing", E)


vw_test_f = open( vw_test_fname,"w")
vw_top_f  = open( vw_top_fname,"w")

vw_g2u_sigs = []
vw_g2u_vals = []
clk_name_arr = []
data_name_arr = []
clk_val_arr = []
data_val_arr_1 = []
data_val_arr = []

# First remove this: { signal: [
sig_arr=wd_file_contents.split('signal:' )

nw_arr=sig_arr[1].split('},')


for val in nw_arr: 

  # { name: 
  name_arr=val.split('name:')
  wave_arr=val.split('wave:')
  #print "val\n"
  #print "NA: name_arr[1]\n"
  #print "WA: wave_arr[1]\n"
  sig_name_arr_1=name_arr[1].split(',')
  sig_name_arr=sig_name_arr_1[0].split('"')
  #print "SIG: sig_name_arr[1]\n"
  vw_g2u_sigs.append(sig_name_arr[1]) 
  wave_val_arr_1 =  wave_arr[1].split(',')
  wave_val_arr = wave_val_arr_1[0].split('"')
  #print "WAVE: wave_val_arr[1]\n"
  vw_g2u_vals.append(wave_val_arr[1])

print("Signal names: ",vw_g2u_sigs  )
print("Signal values:",vw_g2u_vals )

num_sigs = vw_g2u_sigs

per_sig_all_values_arr = []
per_sig_val_arr = []
per_sig_val_arr_1 = []
per_sig_name_arr = []
per_sig_value_count = ""

for w_val  in vw_g2u_vals:
  per_sig_all_values_arr = w_val.split(' ')
  per_sig_value_count = per_sig_all_values_arr
  for per_val_char in per_sig_all_values_arr:

    per_sig_val_arr.append(per_val_char)
    #print "Char: per_val_char\n"

# Replace all . with previous values
prev_char_v = ""
for per_sig_val_arr_i in per_sig_val_arr:
  if per_sig_val_arr_i == "." :
    per_sig_val_arr_1.append(prev_char_v)
  else:
    per_sig_val_arr_1.append(per_sig_val_arr_i)
    prev_char_v = per_sig_val_arr_i
for  per_sig_val_arr_1_i in per_sig_val_arr_1:
  if per_sig_val_arr_1_i == "P":
    clk_val_arr.append(per_sig_val_arr_1_i)
  else:
    data_val_arr_1.append(per_sig_val_arr_1_i)    
for data_val_arr_1_i in data_val_arr_1 :
  if data_val_arr_1_i == "x":
    data_val_arr.append("1'bx")
  elif data_val_arr_1_i == "z":
    data_val_arr.append("1'bz")
  else:
    data_val_arr.append(data_val_arr_1_i)
  
# Separate clock and data name arrays
# BIG Assumption - clock is named "clk"
# Enhance it later
for vw_g2u_sigs_i in vw_g2u_sigs:
  if vw_g2u_sigs_i == vw_clk_sig_name:
    clk_name_arr.append(vw_g2u_sigs_i)
  else: 
    data_name_arr.append(vw_g2u_sigs_i)

for v_per_sig in range(0, len(num_sigs)):
  for v_per_val in range(0,len(per_sig_value_count)):
    per_sig_name_arr.append(vw_g2u_sigs[v_per_sig])


#print " @per_sig_name_arr \n"
#print " @per_sig_val_arr \n"
#print " @per_sig_val_arr_1 \n"
print("Clock name:", clk_name_arr)
print("Clock values:", clk_val_arr)
print("Data sig names:", data_name_arr)
print("Data sig values:", data_val_arr)

uniq_clk_names = unique(clk_name_arr)
vw_clk_sig_name = uniq_clk_names[0]
uniq_data_names = unique(data_name_arr)
uniq_data_sig_count = uniq_data_names
total_data_val_count = data_val_arr
per_sig_val_count =  len(total_data_val_count)/len(uniq_data_sig_count)

def vw_dvc_g2u_if() :
  vw_sv_if_f.write("import uvm_pkg::* ;\n")
  vw_sv_if_f.write("import vw_go2uvm_pkg::* ;\n")
  vw_sv_if_f.write("`include \"uvm_macros.svh\"\n")
  vw_sv_if_f.write("`include \"vw_go2uvm_macros.svh\"\n")
  vw_sv_if_f.write("interface vw_wd_g2u_if();\n")
  for vw_clk_itr in uniq_clk_names:
    vw_sv_if_f.write(f"  logic {vw_clk_itr}; \n" )
  for vw_data_itr in uniq_data_names:
    vw_sv_if_f.write(f"  logic {vw_data_itr};\n")
    vw_sv_if_f.write(f"  default clocking cb @ (posedge {vw_clk_sig_name});\n")
  for vw_data_itr in uniq_data_names: 
    vw_sv_if_f.write(f"    output {vw_data_itr};\n ")
    vw_sv_if_f.write("  endclocking : cb \n")
    vw_sv_if_f.write("endinterface : vw_wd_g2u_if\n") #vw_dvc_g2u_if

def vw_dvc_g2u_test():
  vw_test_f.write("// Generating Go2UVM Test for WaveDrom file: {vw_wd_fname}\n")
  vw_test_f.write("// ---------------------------------------------------------\n")
  vw_test_f.write("// Automatically generated from VerifWorks's DVCreate-Go2UVM product\n")
  vw_test_f.write("// Thanks for using VerifWorks products, see http://www.verifworks.com for more\n")
  vw_test_f.write("import uvm_pkg::*;\n")
  vw_test_f.write("`include \"vw_go2uvm_macros.svh\"\n")
  vw_test_f.write("// Import Go2UVM Package \n")
  vw_test_f.write("import vw_go2uvm_pkg::*;\n")
  vw_test_f.write("// Use the base class provided by the vw_go2uvm_pkg\n")
  vw_test_f.write(f"`G2U_TEST_BEGIN( {vw_test_name}) \n")
  vw_test_f.write("  // Create a handle to the actual interface\n")
  vw_test_f.write(f"  virtual {vw_sv_if_name} vif; \n\n")

  # Code for vif conenction via config_db
  vw_test_f.write("  function void build_phase(uvm_phase phase); \n")
  vw_test_f.write(f"    if (!uvm_config_db#(virtual {vw_sv_if_name})::get( \n")
  vw_test_f.write("      .cntxt(null), .inst_name(\"*\"), \n")
  vw_test_f.write("      .field_name(\"vif\"), .value(vif))) begin : no_vif\n")
  vw_test_f.write("        `g2u_fatal(\"Unable to connect virtual interface to physical interface, check uvm_config_db::set in top module\") \n")
  vw_test_f.write("    end : no_vif \n")
  vw_test_f.write("    else begin : vif_connected \n")
  vw_test_f.write("      `g2u_display(\"Successfully hooked up virtual interface\") \n")
  vw_test_f.write("    end : vif_connected \n")
  vw_test_f.write("  endfunction : build_phase \n\n")


  vw_test_f.write("  task reset;\n")
  vw_test_f.write("    `g2u_display (log_id, \"Start of reset\", UVM_MEDIUM)\n")
  vw_test_f.write("    `g2u_display (log_id, \"Fill in your reset logic here \", UVM_MEDIUM)\n")
  vw_test_f.write("    // this.vif.cb.rst_n <= 1'b0;\n")
  vw_test_f.write("    // repeat (5) @ (this.vif.cb);\n")
  vw_test_f.write("    // this.vif.cb.rst_n <= 1'b1;\n")
  vw_test_f.write("    // repeat (1) @ (this.vif.cb);\n")
  vw_test_f.write("    `g2u_display (log_id, \"End of reset\", UVM_MEDIUM)\n")
  vw_test_f.write("  endtask : reset\n")
  # Move this to test class 
  val_ptr = 0
  vw_sig_count_tmp_1 = 0
  start_val_ptr = 0
  end_val_ptr = 0
  
  for vw_data_itr in uniq_data_names:
    vw_test_f.write(f"  task drive_{vw_data_itr}; \n")
    vw_test_f.write(f"    `g2u_display(\"Driving signal: {vw_data_itr}\") \n")
    start_val_ptr = (vw_sig_count_tmp_1 * per_sig_val_count)
    end_val_ptr = (start_val_ptr)+ (per_sig_val_count - 1)
    for vw_i_1 in range(int(start_val_ptr),int(end_val_ptr)+1):
      vw_test_f.write(f"    vif.{vw_data_itr} <= {data_val_arr[vw_i_1]};\n")
      vw_test_f.write("    @(vif.cb);\n")
  vw_test_f.write(f"    `g2u_display(\"End of stimulus for signal: {vw_data_itr}\") \n")
  vw_test_f.write(f"  endtask : drive_{vw_data_itr} \n\n")
  vw_sig_count_tmp_1=+1
  vw_test_f.write("  task main ();\n")
  vw_test_f.write("    `g2u_display (log_id, \"Start of main\", UVM_MEDIUM)\n")
  vw_test_f.write("    fork \n")
  for vw_data_itr in uniq_data_names:
    vw_test_f.write(f"     drive_{vw_data_itr}; \n")
  vw_test_f.write("    join \n")
  vw_test_f.write("    // this.vif.cb.inp_1 <= 1'b0;\n")
  vw_test_f.write("    // this.vif.cb.inp_2 <= 22;\n")
  vw_test_f.write("    // repeat (5) @ (this.vif.cb);\n")
  vw_test_f.write("    `g2u_display (log_id, \"End of main\", UVM_MEDIUM)\n")
  vw_test_f.write("  endtask : main\n")
  vw_test_f.write("`G2U_TEST_END \n")
def vw_dvc_g2u_top_mod():
  mod_name   =   vw_top_name
  vw_top_f.write( f"// Generating Go2UVM top module for DUT: {mod_name}\n")
  vw_top_f.write( "// ---------------------------------------------------------\n")
  vw_top_f.write( f"module {mod_name};\n")
  vw_top_f.write( "  timeunit 1ns;\n")
  vw_top_f.write( "  timeprecision 1ns;\n")
  vw_top_f.write( "  parameter VW_CLK_PERIOD = 10;\n")
  vw_top_f.write( "  // Simple clock generator\n")
  vw_top_f.write( f"  bit {vw_clk_sig_name} ;\n")
  vw_top_f.write( f"  always # (VW_CLK_PERIOD/2) {vw_clk_sig_name} <= ~{vw_clk_sig_name};\n")
  vw_top_f.write( "  // Interface instance\n")
  vw_top_f.write( f" {vw_sv_if_name} {vw_sv_if_name}_0. (.*);\n")
  vw_top_f.write( f"  assign {vw_sv_if_name}_0.{vw_clk_sig_name} = {vw_clk_sig_name}; \n\n") 
  vw_top_f.write( "  // Using VW_Go2UVM\n")
  vw_top_f.write( f"  {vw_test_name} {vw_test_name}_0;\n")
  vw_top_f.write( "  initial begin : go2uvm_test\n")
  vw_top_f.write( f"    {vw_test_name}_0 = new (); \n\n")
  vw_top_f.write( "    // Connect virtual interface to physical interface\n")
  vw_top_f.write( f"    uvm_config_db#(virtual {vw_sv_if_name})::set( \n")
  vw_top_f.write(  "     .cntxt(null), .inst_name(\"*\"), \n")
  vw_top_f.write( f"     .field_name(\"vif\"), .value({vw_sv_if_name}_0)); \n\n" )
  vw_top_f.write( "    // Kick start standard UVM phasing\n")
  vw_top_f.write( "    run_test ();\n")
  vw_top_f.write( "  end : go2uvm_test\n")
  vw_top_f.write( f"endmodule : {mod_name} \n")

def PrintMakeFile() :
  print("Working on Makefile...")
  text ="""
  VCS != vcs
  os.system("clean: crm -fr csrc* DVE* scsim* led* simv* ucli* inter*  work* *.cm *.daidir *.h vsim.wlf transcript INCA* *.log *.vstf *.key waves.shm dataset* *.cfg .athdl* *.txt* athdl_sv* *~* *.db* compile *.awc .simvision*")

  cvc1:clean
	  \(VCS) -timescale=1ns/1ns -sverilog -debug_all -lca -ntb_opts uvm-1.1 -f vw_flist_fname -l comp.log
	  ./simv +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_FULL -l vcs.log

  cvc1_gui:
	  ./simv +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_HIGH -l vcs.log -gui &


  cvc2:clean
	  vlib work
	  vlog +acc -sv -mfcu -f vw_flist_fname | tee comp.log 
	  vsim -c -assertdebug +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_HIGH vw_top_name -do "run -aquit" -l g2u_comp.log 


  cvc2_gui:clean
	  vlib work
	  vlog +acc -sv -mfcu -f vw_flist_fname 
	  vsim -assertdebug +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_HIGH vw_top_name -do "run -a" -l g2u_comp.log 
	  vcover report -html fcover.ucdb
	  firefox covhtmlreport/index.html -l qsta.log

  cvc3:clean
	  irun -access +rw -uvm -f vw_flist_fname +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_HIGH -coverage all -l cadence.log

  cvc3_gui:clean
	  irun -access +rw -uvm -f vw_flist_fname +UVM_TESTNAME=vw_test_name +UVM_VERBOSITY=UVM_HIGH -coverage all -l cadence.log -gui &


  cvc4:clean
	  vsim -c -do rvra_run.do
	  firefox fcover_report.html 

  cvc4_gui:clean
	  vsim -do rvra_run.do"""

  vw_make_f.write(text)
  print("Makefile created successfully.") # PrintMakeFile

def PrintFlist():
  vw_flist_f.write("+incdir+\VW_GO2UVM_HOME/src")
  vw_flist_f.write("\VW_GO2UVM_HOME/src/vw_go2uvm_pkg.sv")
  vw_flist_f.write("vw_sv_if_fname ")
  vw_flist_f.write("vw_test_fname ")
  vw_flist_f.write("vw_top_fname ")
# PrintFlist

#main body
#create interface file
vw_dvc_g2u_if()
vw_sv_if_f.close()

# Create Go2UVM Test file
vw_dvc_g2u_test()
vw_test_f.close()

# Create Top module 
vw_dvc_g2u_top_mod()
vw_top_f.close()

# Create Go2UVM Makefile
PrintMakeFile ()
vw_make_f.close()
PrintFlist()
vw_flist_f.close()
