#generate stats based on a parity log file
import sys, re
if len(sys.argv) < 2:
    print("needs a parity log filename as an argument")
    sys.exit()

stats_regexp = re.compile("{0} txs, {0} Mgas, {0} ms, {0} KiB".format("(\d+(?:\.\d*)?)"))
imported_blocks = 0
mgas_used = 0
verification_time_ms = 0
kB_used = 0
for line in open(sys.argv[1], 'r'):
    if "Imported" in line: #not synced block
        d = line[line.find('(')+1:line.find(')')]
        txs, mgas, ms, size = stats_regexp.match(d).groups()
        imported_blocks += 1
        mgas_used += float(mgas)
        verification_time_ms += float(ms)
        kB_used += float(size)
verification_time_s = verification_time_ms/1000
avg_mgas_s = mgas_used/verification_time_s
avg_block_verification_time_ms = verification_time_ms/imported_blocks
avg_kBps = kB_used/verification_time_s
print("Average speed %f Mgas/s, %f kB/s" % (avg_mgas_s, avg_kBps))
print("Average block verification time %f ms" % avg_block_verification_time_ms)
