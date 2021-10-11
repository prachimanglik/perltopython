
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
	  vsim -do rvra_run.do