import sys
import regex


def main(fname, miss_num):
    # Same file opened two times with different file descriptor
    fd = open(fname, 'r')
    fc = open(fname, 'r')

    for lines in fd:
        for i in range(50, 1, -1):
            for j in range(0, 50, i):
                out = False

                # Avoid segment of NON correct length
                if j + i > 50:
                    break

                #  Check in all lines of the file
                for cline in fc:
                    segment = lines[j:j+i]
                    if not match(cline, segment, miss_num):
                        out = True
                        break

                # If match find exit
                if not out:
                    print("Longest Match: %s #%d" % (segment, len(segment)))
                    exit(0)

                fc.seek(0)
    fd.close()
    fc.close()


def match(sequence, segment, miss=0):
    # Fuzzy regex with #miss possible substitutions
    pattern = r"(%s){s<=%d}" % (segment, miss)
    return regex.findall(pattern, sequence, overlapped=True)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
