filename = 'scripts/data.txt'

with open(filename, mode='r') as f:
    with open('out.txt', 'a') as f_out:

        content = f.readlines()

        for line in content:
            line = line.rstrip('\n')
            print(line, end='\n--------------------\n')

            if 'a' in line:
                f_out.write(line + '\n')
                print(line, file=f_out)


