#!/usr/bin/python
import re

rc = open("root_complex_compile.do");
dev = open("iprop_nvme_dev_ref_design_wrapper_compile.do");

search_string = re.compile(r'\bmsim\/\w*\b');
rc_msim_libs = [];
#dev_msim_libs = [];

# append strings to rc_msim_args
for line in rc:
    match_string_list = search_string.findall(line);
    if (match_string_list != [])is True:
        # each match list should only have 1 item
        # we want a list of strings not a list of items
        rc_msim_libs.append(match_string_list[0]);

print "rc libs: ",rc_msim_libs;
print "***********************"

# append strings to rc_msim_args
for line in dev:
    match_string_list = search_string.findall(line);
    if (match_string_list != [])is True:
        # each match list should only have 1 item
        # we want a list of strings not a list of items
        rc_msim_libs.append(match_string_list[0]);

print "dev libs: ",rc_msim_libs;
print "***********************"

rc_msim_libs = list(set(rc_msim_libs));

# make runsim string
runsim_string = "vsim -c -novopt cmd_controller xil_defaultlib.glbl";

for lib in rc_msim_libs:
    runsim_string = runsim_string + " -L " + lib;

runsim_string = runsim_string + "log -r *; run ${1}; quit;";

# close .do files
rc.close();
dev.close();

# write runsim_string to file
file_out = open('runsim','w');
file_out.write(runsim_string);
file_out.close();
