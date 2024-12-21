import network
import time
import random
import pandas as pd
from plotly import graph_objs as go
#import plotly.graph_objects as go
import networkx as nx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
from numpy import sqrt
import glob
import random
from tkinter import messagebox

random.seed(7)
np.random.seed(7)

def get_initial_centroids(X, k):
    number_of_samples = X.shape[0]
    sample_points_ids = random.sample(range(0, number_of_samples), k)

    centroids = [tuple(X[id]) for id in sample_points_ids]
    unique_centroids = list(set(centroids))

    number_of_unique_centroids = len(unique_centroids)

    while number_of_unique_centroids < k:
        new_sample_points_ids = random.sample(range(0, number_of_samples), k - number_of_unique_centroids)
        new_centroids = [tuple(X[id]) for id in new_sample_points_ids]
        unique_centroids = list(set(unique_centroids + new_centroids))

        number_of_unique_centroids = len(unique_centroids)

    return np.array(unique_centroids)


def distance_calculation(A_matrix, B_matrix):
    A_square = np.reshape(np.sum(A_matrix * A_matrix, axis=1), (A_matrix.shape[0], 1))
    B_square = np.reshape(np.sum(B_matrix * B_matrix, axis=1), (1, B_matrix.shape[0]))
    AB = A_matrix @ B_matrix.T

    C = -2 * AB + B_square + A_square

    return np.sqrt(C)


def get_ip_clusters(X, centroids, distance_mesuring_method):
    k = centroids.shape[0]

    clusters = {}

    distance_matrix = distance_mesuring_method(X, centroids)

    closest_cluster_ids = np.argmin(distance_matrix, axis=1)

    for i in range(k):
        clusters[i] = []

    for i, cluster_id in enumerate(closest_cluster_ids):
        clusters[cluster_id].append(X[i])

    return clusters


def has_centroids_covered(previous_centroids, new_centroids, distance_mesuring_method, movement_threshold_delta):
    distances_between_old_and_new_centroids = distance_mesuring_method(previous_centroids, new_centroids)
    centroids_covered = np.max(distances_between_old_and_new_centroids.diagonal()) <= movement_threshold_delta

    return centroids_covered


def perform_LA_AHD(X, k, distance_mesuring_method, movement_threshold_delta=0):
    new_centroids = get_initial_centroids(X=X, k=k)

    centroids_covered = False

    while not centroids_covered:
        previous_centroids = new_centroids
        clusters = get_ip_clusters(X, previous_centroids, distance_mesuring_method)

        new_centroids = np.array([np.mean(clusters[key], axis=0, dtype=X.dtype) for key in sorted(clusters.keys())])

        centroids_covered = has_centroids_covered(previous_centroids, new_centroids, distance_mesuring_method, movement_threshold_delta)

    return new_centroids


def get_reduced_indexers(node, datapackets_count):

    h, w, d = node.shape

    X = np.reshape(node, (h * w, d))
    X = np.array(X, dtype=np.int32)

    centroids = perform_LA_AHD(X, k=datapackets_count, distance_mesuring_method=distance_calculation, movement_threshold_delta=4)
    distance_matrix = distance_calculation(X, centroids)
    closest_cluster_ids = np.argmin(distance_matrix, axis=1)

    X_reconstructed = centroids[closest_cluster_ids]
    X_reconstructed = np.array(X_reconstructed, dtype=np.uint8)
    reduced_image = np.reshape(X_reconstructed, (h, w, d))

    return reduced_image


nodes = int(input("Enter number of nodes : "))
nodes=nodes
#tot_nodes=nodes+4
print('*************************************************')
print('******************Nodes List*********************')
print('*************************************************')
nodeslist=[]

for i in range(nodes):
    print('Node h'+str(i+1)+' has been created')
    time.sleep(2.4)
    print('Node h'+str(i+1)+' has been started')
    time.sleep(2.4)
    nodeslist.append('h'+str(i+1))


switches = 4
switcheslist=[]
if nodes<switches:
    print("Anchor should be less than nodes. Rerun")
else:    
    print('*************************************************')
    print('****************Anchor Nodes List********************')
    print('*************************************************')
    switcheslist=[]
    for i in range(switches):
        print('Anchor A'+str(i+1)+' has been created')
        time.sleep(2.4)
        switcheslist.append('A'+str(i+1))


    print('*************************************************')
    print('****************Anchor Mapping*****************')
    print('*************************************************')
    mapperslist=[]
    for i in range(nodes):
        switchname=random.choice(switcheslist)
        print('(h'+str(i+1)+','+switchname+')')
        mapperslist.append('(h'+str(i+1)+','+switchname+')')

    print('*************************************************')
    print('****************Request Generation***************')
    print('*************************************************')
    import random
    from ipaddress import IPv4Address


    def _random_ip_address(seed):
        random.seed(seed)
        return str(IPv4Address(random.getrandbits(32)))


    def is_valid(ip):
     
        # Splitting by "."
        ip = ip.split(".")
         
        # Checking for the corner cases
        for i in ip:
            if (len(i) > 3 or int(i) < 0 or
                              int(i) > 255):
                return False
            if len(i) > 1 and int(i) == 0:
                return False
            if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
                return False
                 
        return True
     
    # Function converts string to IP address
    def convert(s):
         
        sz = len(s)
     
        # Check for string size
        if sz > 12:
            return []
        snew = s
        l = []
     
        # Generating different combinations.
        for i in range(1, sz - 2):
            for j in range(i + 1, sz - 1):
                for k in range(j + 1, sz):
                    snew = snew[:k] + "." + snew[k:]
                    snew = snew[:j] + "." + snew[j:]
                    snew = snew[:i] + "." + snew[i:]
                     
                    # Check for the validity of combination
                    if is_valid(snew):
                        l.append(snew)
                         
                    snew = s
                     
        return l

    iplist=[]
    ipcount=nodes+4
    for i in range(ipcount):
        ipval4=str(random.randint(0,255))
        ipval1=str(random.randint(0,255))
        ipval2=str(random.randint(0,255))
        ipval3=str(random.randint(0,255))
        ipval=str(ipval1)+"."+str(ipval2)+"."+str(ipval3)+"."+str(ipval4)
        print(ipval)
        iplist.append(ipval)
    print('*************************************************')
    print('****************Ipaddress List*******************')
    print('*************************************************')
    for i in range(len(iplist)):
        print(iplist[i])
    print('*************************************************')
    print('****************Power Sharing List****************')
    print('*************************************************')
    anchlist=[]
    for i in range(len(iplist)-4,len(iplist)):
        anchlist.append(iplist[i])
    for i in range(len(anchlist)):
        print(anchlist[i])
    
    print('*************************************************')
    
    print('*************************************************')
    reqlist=[]
    rlist=[]
    tolist=[]
    '''
    if nodes==20: 
    	req = nodes+6
    elif nodes==10:
    	req = nodes-1
    else:
    '''
    req = 60
    for i in range(req):
        ip1=str(random.choice(iplist))
        ip2=str(random.choice(iplist))
        reqval=ip1+"--------------->"+ip2        
        messagebox.showinfo("showinfo", "Overload occured at "+str(ip1)+" unloading to "+str(ip2))
        if i%25==0:
            messagebox.showinfo("showinfo", "Incident captured at "+str(ip1))
            
        print(reqval)
        reqlist.append(reqval)
        rlist.append(ip1)
        tolist.append(ip2)
    df = pd.DataFrame(rlist, columns=["Ipaddress"])
    reqvalperf=df.groupby(by=["Ipaddress"]).sum()
    print(reqvalperf)
    df.groupby(by=["Ipaddress"]).sum()
    import pandas as pd
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.erdos_renyi_graph(20, 1)
    #df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})
    df = pd.DataFrame({ 'from':rlist, 'to':tolist})
    G = nx.from_pandas_edgelist(df, 'from', 'to')
    print('---------------------------')
    color_map = []
    for node in G:
        if node==anchlist[0]:
            color_map.append('red')
        elif node==anchlist[1]:
            color_map.append('red')
        elif node==anchlist[2]:
            color_map.append('red')
        elif node==anchlist[3]:
            color_map.append('red')
        else: 
            color_map.append('green')

    #Adding fixed positions
    fixed_positions = {anchlist[0]:(0,0),anchlist[1]:(0,4),anchlist[2]:(4,4),anchlist[3]:(4,0)}#dict with two of the positions set
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)
    '''
    for node in G:
        for n in anchlist:
            print(node)
            print(n)
            if node==n:
                color_map.append('red')
            else: 
                color_map.append('green')
    '''
    print(len(color_map))
    nx.draw(G,pos, node_color=color_map, with_labels=True)
    plt.show()




    '''
     
    # ------- DIRECTED
     
    # Build a dataframe with your connections
    # This time a pair can appear 2 times, in one side or in the other!
    df = pd.DataFrame({ 'from':rlist, 'to':tolist})
     
    # Build your graph. Note that we use the DiGraph function to create the graph!
    G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph() )
     
    # Make the graph
    nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
    plt.title("Directed")
    plt.show()
     
    # ------- UNDIRECTED
     
    # Build a dataframe with your connections
    # This time a pair can appear 2 times, in one side or in the other!
    df = pd.DataFrame({ 'from':rlist, 'to':tolist})
     
    # Build your graph. Note that we use the Graph function to create the graph!
    G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph() )
     
    # Make the graph
    nx.draw(G, with_labels=True, node_size=1500, alpha=0.3, arrows=True)
    plt.title("UN-Directed")
    plt.show()
    '''
    print('*************************************************')
    print('*********Power Exchange Collections*******************')
    print('*************************************************')
    for i in range(6):
        print(random.choice(reqlist))

    print('run python pyexcel.py '+str(nodes))



path = 'icons/'
files = [f for f in glob.glob(path + "*.png")]
img = []
for f in files:
    img.append(mpimg.imread(f))
N = 30#len(files)
imgcount=len(files)

# generate graph
G = nx.watts_strogatz_graph(N,4,0.2)
pos=nx.spring_layout(G,k=3/sqrt(N))

# draw with images on nodes
nx.draw_networkx(G,pos,width=3,edge_color="r",alpha=0.6)
ax=plt.gca()
fig=plt.gcf()
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.1 # this is the image size
for n in G.nodes():
    (x,y) = pos[n]
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(random.choice(img))
    a.set_aspect('equal')
    a.axis('off')
plt.show()
       
