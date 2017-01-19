import numpy as np

start_idx = 24
num_width = 20
space_width = 1
gs_start = -7
w_stdev = .3
w_max = 0.5


f = open("hm_obsS.dat",'r')
f_ins = open("stage_A.ins",'w')
f_obs = open("pest_obs.dat",'w')
f_ins.write("pif ~\n")
header = f.readline().strip().split() #header
obs_lines = []
grps = ["regul"]
nobs = 0
for i,line in enumerate(f):
	line = line.strip().split()
	site = line[0]
	#obs_name = "imas_{0:03d}".format(i+1)
	if i == 0:
		f_ins.write("l2 ")
	else:
		f_ins.write("l1 ")
	gs = gs_start
	for ival in range(4,len(line)):
		val = float(line[ival])
		s_idx = ((num_width+space_width) * (ival-1)) + 1
		e_idx = s_idx + num_width + space_width - 1
		if ival == 4:
			obs_name = site+'_imas'
			grp = "imas"
		else:
			if gs < 0:
				obs_name = site+'_n{0:01d}'.format(np.abs(gs))
				grp = "gs_n"+str(np.abs(gs))
			else:
				obs_name = site+'_{0:02d}'.format(gs)
				grp = "gs_"+str(gs)
			gs += 1
		if val != 0.0:
			w = min(1.0 / (val * w_stdev),w_max)
		else:
			w = w_max
		if grp not in grps:grps.append(grp)
		ins_string = '['+obs_name+']'+str(s_idx)+':'+str(e_idx) 
		f_ins.write("{0:25s}".format(ins_string))
		#f_obs.write("{0:25s} {1:15.6E} {2:15.6E} {3:10s}\n".format(obs_name,val,w,grp))
		obs_lines.append("{0:25s} {1:15.6E} {2:15.6E} {3:10s}\n".format(obs_name,val,w,grp))
		nobs += 1
	f_ins.write('\n')

		 #["+obs_name+"]67:87\n")
	#f_obs.write(obs_name+' {0:15.6E}  {1:15.6E} imas\n'.format(val,1.0/val))
f.close()
f = open("kirishima_samples.xyz2.utm.shift",'r')
grp = "imas_2"
grps.append(grp)
for iline,line in enumerate(f):
	line = line.strip().split()
	obs_name = "imas_{0:02d}".format(iline+1)
	val = float(line[-1])
	s_idx = ((num_width+space_width) * (3)) + 1
	e_idx = s_idx + num_width + space_width - 1
	if val != 0.0:
		w = min(1.0 / (val * w_stdev),w_max)
	else:
		w = w_max

	ins_string = 'l1 ['+obs_name+']'+str(s_idx)+':'+str(e_idx) 
	f_ins.write("{0:25s}\n".format(ins_string))
	obs_lines.append("{0:25s} {1:15.6E} {2:15.6E} {3:10s}\n".format(obs_name,val,w,grp))
	nobs += 1
f_ins.close()
f_obs.write("* observation groups\n")
for grp in grps:
	f_obs.write(grp+'\n')
f_obs.write("* observation data\n")
for oline in obs_lines:
	f_obs.write(oline)

print "nobs",nobs
f_obs.close()	