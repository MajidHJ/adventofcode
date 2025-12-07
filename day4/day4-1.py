import os
import io
base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
spath = os.path.join(base, 'sample.txt')
opath = os.path.join(base, 'output.txt')



def check_middle (rows:list,l,idx):
    roll_counter = 0
    adj = {
    'NW' : rows[l-1][idx-1],
    'NN' : rows[l-1][idx],
    'NE' : rows[l-1][idx+1],
    'WW' : rows[l][idx-1],
    'EE' : rows[l][idx+1],
    'SW' : rows[l+1][idx-1],
    'SS' : rows[l+1][idx],
    'SE' : rows[l+1][idx+1]
    }

    for i in adj:
        if adj[i]=='@':
            roll_counter +=1
    if roll_counter >3 :
        return False
    else:
        return True
    
def check_borders(rows,l,idx):

    roll_counter = 0
    adj = {
    'WW' : rows[l][idx-1],
    'EE' : rows[l][idx+1],
    'SW' : rows[l+1][idx-1],
    'SS' : rows[l+1][idx],
    'SE' : rows[l+1][idx+1]
    }

    for i in adj:
        if adj[i]=='@':
            roll_counter +=1
    if roll_counter >3 :
        return False
    else:
        return True


total_sum = 0

def scan(content:str):
    global total_sum
    local_sum = 0
    lookup_table = []
    lines = content.splitlines()
    lncount = len(lines)

    def get_lines(frm,too) :
        rows = []
        for i in range(frm,too):
            line = lines[i]
            rows.append(line)
        return rows

    def get_corners():
         
        topline = lines[0]
        botline = lines[-1]
        corners = {topline[0]:(0,0),topline[-1]:(0,lncount-1),botline[0]:(lncount-1,0),botline[-1]:(lncount-1,lncount-1)}
        return corners

    def check (rows:list,target,checker_function):
        ssum = 0
        found_idxs = []
        for idx,char in enumerate(rows[target][1:-1],1):
            if char == '@' :
                if checker_function(rows,target,idx) :
                    found_idxs.append(idx)
                    ssum +=1       
        return found_idxs

# check middle charakcers

    for i in range(1,lncount-1):
        rows = get_lines(i-1,i+2)
        found_idxs = check(rows,1,check_middle)       
        local_sum += len(found_idxs)
        lookup_table.extend([(i,x) for x in found_idxs])

        
# check first line   
    rows = get_lines(0,2)
    found_idxs = check(rows,0,check_borders)
    local_sum += len(found_idxs)
    lookup_table.extend([(0,x) for x in found_idxs])    



# check last line
    r =get_lines(lncount-2,lncount)
    rows = [r[1],r[0]]
    found_idxs = check(rows,0,check_borders)
    local_sum += len(found_idxs)
    lookup_table.extend([(lncount-1,x) for x in found_idxs])   


#check left column
    ll = ''
    lr = ''
    rows = []
    for i in range(lncount):
        line = lines[i]
        ll += line[:1]
        lr += line[1:2]
    rows.append(ll)
    rows.append(lr)

    found_idxs = check(rows,0,check_borders)
    local_sum += len(found_idxs)
    lookup_table.extend([(x,0) for x in found_idxs])
    
# check right column
    rr = ''
    rl = ''
    rows = []
    for i in range(lncount):
        line = lines[i]
        rr += line[len(line)-1:]
        rl += line[len(line)-2:len(line)-1]
    rows.append(rr)
    rows.append(rl)

    found_idxs = check(rows,0,check_borders)
    local_sum += len(found_idxs)
    lookup_table.extend([(x,lncount-1) for x in found_idxs])

    corners = get_corners()
    
    for i in corners :
        if i=='@' :
            local_sum +=1
            lookup_table.append(corners[i])

    
    
    page = []

    for i in lines:
        page.append(list(i))

    for i in lookup_table:
        r = i[0]
        c = i[1]
        page[r][c] = 'X'

    string_page = ''

    for i in page:
        string_page += ''.join(i)+'\n'
    

    print(local_sum)
    print(string_page)
    total_sum += local_sum
    print('----------------------------')
    if local_sum ==0 : return
    scan(string_page)
    
    



path = ipath

with open(path,'r') as f:
    content = f.read()
    scan(content)
    print(total_sum)