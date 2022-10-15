clean:
	rm *.e* *.o*

check_q:
	@echo -n "items in queue: "
	@qstat | wc -l
	@echo -n "queue gpu_1 jobs: "
	@qstat | grep gpu_1 | wc -l
	@echo -n "queue STDIN jobs: "
	@qstat | grep STDIN | wc -l		
