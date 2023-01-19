# Step 1 - Import the library:
from sklearn.linear_model import LinearRegression
# Step 2 - Create an instance of the model:
model = LinearRegression()
# Step 3 - Train the model:
import pandas as pd

df = pd.read_csv("../data/UNSW_NB15_training-set.csv", encoding='utf-8',low_memory=False)
# PreData 
df['attack_cat']=df['attack_cat'].replace(['Normal','Analysis','Backdoor','DoS','Exploits','Fuzzers',"Generic",'Reconnaissance','Shellcode','Worms'],[0,1,2,3,4,5,6,7,8,9])

model = model.fit( df[ ["dur", "proto", "service", "state", "spkts", "sbytes", "dbytes", "rate", "sttl"] ], df["attack_cat"])
# dur	proto	service	state	spkts	dpkts	sbytes	dbytes	rate	sttl	dttl	sload	dload	sloss	dloss	sinpkt	dinpkt	sjit	djit	swin	stcpb	dtcpb	dwin	tcprtt	synack	ackdat	smean	dmean	trans_depth	response_body_len	ct_srv_src	ct_state_ttl	ct_dst_ltm	ct_src_dport_ltm	ct_dst_sport_ltm	ct_dst_src_ltm	is_ftp_login	ct_ftp_cmd	ct_flw_http_mthd	ct_src_ltm	ct_srv_dst	is_sm_ips_ports


# Step 4 - Predict the outcome:

data = []
data.append( {
    "dur": 0.217978, 
    "proto": 114, 
    "service": 6, 
    "state": 3, 
    "spkts": 10,
    "sbytes": 6, 
    "dbytes": 802, 
    "rate": 268, 
    "sttl": 68.814284
    } )
df2 = pd.DataFrame(data)

# Add a new column to `df2` with the predicted result:
df2["result_predict"] = model.predict(df2)

# Display `df2` to see our results:
print(df2)