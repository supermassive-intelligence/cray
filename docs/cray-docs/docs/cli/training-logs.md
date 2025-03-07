# Training Logs

```console
./cray llm logs -f
```

This command streams the training logs for the model with the specified identifier. The logs include information about the training process, such as the loss and accuracy of the model at each epoch.

If no identifiers are provided, the command will list the most recent model.

```console
0 + export CRAY_TRAINING_JOB_CONFIG_PATH=/app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/config.yaml
1 + CRAY_TRAINING_JOB_CONFIG_PATH=/app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/config.yaml
2 +++ dirname /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/config.yaml
3 ++ cd /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e
4 ++ pwd
5 + LOCAL_DIRECTORY=/app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e
6 + export PYTHONPATH=/app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/ml::/app/cray/infra:/app/cray/sdk:/app/cray/ml
7 + PYTHONPATH=/app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/ml::/app/cray/infra:/app/cray/sdk:/app/cray/ml
8 + mpirun --allow-run-as-root python /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/ml/cray_megatron/main.py
9 INFO:cray_infra.training.print_logo:
10 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⢀⡐⢄⢢⡐⢢⢁⠂⠄⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
11 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⡄⣌⠰⣘⣆⢧⡜⣮⣱⣎⠷⣌⡞⣌⡒⠤⣈⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
12 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠊⠀⠀⠀⠀⢀⠢⠱⡜⣞⣳⠝⣘⣭⣼⣾⣷⣶⣶⣮⣬⣥⣙⠲⢡⢂⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
13 ⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⢀⠢⣑⢣⠝⣪⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣻⢦⣍⠢⢅⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
14 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢆⡱⠌⣡⢞⣵⣿⣿⣿⠿⠛⠛⠉⠉⠛⠛⠿⢷⣽⣻⣦⣎⢳⣌⠆⡱⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
15 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠠⠌⢢⢃⡾⣱⣿⢿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣏⠻⣷⣬⡳⣤⡂⠜⢠⡀⣀⠀⠀⡀⠀⠀⠀⠀⠀⠀
16 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⣌⢃⡾⢡⣿⢣⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⡊⣿⣿⣾⣽⣛⠶⣶⣬⣭⣥⣙⣚⢷⣶⠦⡤⢀
17 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠂⠰⡌⡼⠡⣼⢃⡿⠀⠀⠀⠀MasInt⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠿⣛⣯⡴⢏⠳⠁⠀
18 ⠀⠀⠀⠀⠀⠀⠀⠀⠠⠑⡌⠀⣉⣾⣩⣼⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣿⣿⣿⣿⡿⢛⣛⣯⣭⠶⣞⠻⣉⠒⠀⠂⠀⠀⠀
19 ⠀⠀⠀⠀⠀⠀⢀⣀⡶⢝⣢⣾⣿⣼⣿⣿⣿⣿⣿⣀⣼⣀⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠿⡛⠏⠍⠂⠁⢠⠁⠀⠀⠀⠀⠀⠀⠀
20 ⠀⠠⢀⢥⣰⣾⣿⣯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣽⠟⣿⠐⠨⠑⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
21 ⡐⢢⣟⣾⣿⣿⣟⣛⣿⣿⣿⣿⢿⣝⠻⠿⢿⣯⣛⢿⣿⣿⣿⡛⠻⠿⣛⠻⠛⡛⠩⢁⣴⡾⢃⣾⠇⢀⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
22 ⠈⠁⠊⠙⠉⠩⠌⠉⠢⠉⠐⠈⠂⠈⠁⠉⠂⠐⠉⣻⣷⣭⠛⠿⣶⣦⣤⣤⣴⣴⡾⠟⣫⣾⣿⡏⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
23 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⢿⢶⣤⣬⣉⣉⣭⣤⣴⣿⣿⡿⠃⠄⡈⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
24 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠘⢊⠳⠭⡽⣿⠿⠿⠟⠛⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
25 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠈⠐⠀⠘⠀⠈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
26
27 DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): huggingface.co:443
28 DEBUG:urllib3.connectionpool:https://huggingface.co:443 "HEAD /NousResearch/Llama-3.2-1B/resolve/main/tokenizer_config.json HTTP/1.1" 200 0
29 `loss_type=None` was set in the config but it is unrecognised.Using the default loss: `ForCausalLMLoss`.
30 INFO:cray_megatron.megatron.training_loop:Training step 0 - epoch 0 - loss 11.851648330688477- learning rate 0.003
31 INFO:cray_megatron.megatron.training_loop:Training step 1 - epoch 0 - loss 11.491947174072266- learning rate 0.0029850000000000002
32 INFO:cray_megatron.megatron.training_loop:Training step 2 - epoch 1 - loss 11.067758560180664- learning rate 0.00297
33 INFO:cray_megatron.megatron.training_loop:Training step 3 - epoch 2 - loss 10.38668155670166- learning rate 0.0029549999999999997
34 INFO:cray_megatron.megatron.training_loop:Training step 4 - epoch 3 - loss 10.309948921203613- learning rate 0.0029399999999999995
35 INFO:cray_megatron.megatron.training_loop:Training step 5 - epoch 4 - loss 10.753833770751953- learning rate 0.0029249999999999996
36 INFO:cray_megatron.megatron.training_loop:Training step 6 - epoch 5 - loss 11.955288887023926- learning rate 0.00291
37 INFO:cray_megatron.megatron.training_loop:Training step 7 - epoch 6 - loss 10.206552505493164- learning rate 0.002895
38 INFO:cray_megatron.megatron.training_loop:Training step 8 - epoch 7 - loss 11.689804077148438- learning rate 0.0028799999999999997
39 INFO:cray_megatron.megatron.training_loop:Training step 9 - epoch 8 - loss 11.29571533203125- learning rate 0.0028649999999999995
40 INFO:cray_megatron.megatron.training_loop:Training step 10 - epoch 9 - loss 9.205053329467773- learning rate 0.0028499999999999997
41 INFO:cray_megatron.megatron.training_loop:Training step 11 - epoch 10 - loss 11.743261337280273- learning rate 0.0028349999999999994
42 INFO:cray_megatron.megatron.training_loop:Training step 12 - epoch 11 - loss 8.788749694824219- learning rate 0.002819999999999999
43 INFO:cray_megatron.megatron.training_loop:Training step 13 - epoch 12 - loss 9.033876419067383- learning rate 0.002804999999999999
44 INFO:cray_megatron.megatron.training_loop:Training step 14 - epoch 13 - loss 11.744029998779297- learning rate 0.0027899999999999986
45 INFO:cray_megatron.megatron.training_loop:Training step 15 - epoch 14 - loss 8.629796981811523- learning rate 0.002774999999999999
46 INFO:cray_megatron.megatron.training_loop:Training step 16 - epoch 15 - loss 8.350188255310059- learning rate 0.002759999999999999
47 INFO:cray_megatron.megatron.training_loop:Training step 17 - epoch 16 - loss 8.093982696533203- learning rate 0.0027449999999999987
48 INFO:cray_megatron.megatron.training_loop:Training step 18 - epoch 17 - loss 7.8525495529174805- learning rate 0.002729999999999999
49 INFO:cray_megatron.megatron.training_loop:Training step 19 - epoch 18 - loss 11.577287673950195- learning rate 0.002714999999999999
50 INFO:cray_megatron.megatron.training_loop:Training step 20 - epoch 19 - loss 7.367895126342773- learning rate 0.0026999999999999993
51 INFO:cray_megatron.megatron.training_loop:Training step 21 - epoch 20 - loss 11.79365348815918- learning rate 0.0026849999999999995
52 INFO:cray_megatron.megatron.training_loop:Training step 22 - epoch 21 - loss 6.936058044433594- learning rate 0.002669999999999999
53 INFO:cray_megatron.megatron.training_loop:Training step 23 - epoch 22 - loss 10.056737899780273- learning rate 0.0026549999999999994
54 INFO:cray_megatron.megatron.training_loop:Training step 24 - epoch 23 - loss 9.305437088012695- learning rate 0.0026399999999999996
55 INFO:cray_megatron.megatron.training_loop:Training step 25 - epoch 24 - loss 6.2938947677612305- learning rate 0.0026249999999999993
56 INFO:cray_megatron.megatron.training_loop:Training step 26 - epoch 25 - loss 6.068697929382324- learning rate 0.0026099999999999995
57 INFO:cray_megatron.megatron.training_loop:Training step 27 - epoch 26 - loss 5.812913417816162- learning rate 0.0025949999999999992
58 INFO:cray_megatron.megatron.training_loop:Training step 28 - epoch 27 - loss 10.825139999389648- learning rate 0.002579999999999999
59 INFO:cray_megatron.megatron.training_loop:Training step 29 - epoch 28 - loss 9.760759353637695- learning rate 0.002564999999999999
60 INFO:cray_megatron.megatron.training_loop:Training step 30 - epoch 29 - loss 10.444537162780762- learning rate 0.0025499999999999993
61 INFO:cray_megatron.megatron.training_loop:Training step 31 - epoch 30 - loss 9.888254165649414- learning rate 0.0025349999999999995
62 INFO:cray_megatron.megatron.training_loop:Training step 32 - epoch 31 - loss 4.675031661987305- learning rate 0.0025199999999999992
63 INFO:cray_megatron.megatron.training_loop:Training step 33 - epoch 32 - loss 4.461902618408203- learning rate 0.0025049999999999994
64 INFO:cray_megatron.megatron.training_loop:Training step 34 - epoch 33 - loss 4.232550621032715- learning rate 0.002489999999999999
65 INFO:cray_megatron.megatron.training_loop:Training step 35 - epoch 34 - loss 9.657859802246094- learning rate 0.0024749999999999993
66 INFO:cray_megatron.megatron.training_loop:Training step 36 - epoch 35 - loss 5.435771942138672- learning rate 0.002459999999999999
67 INFO:cray_megatron.megatron.training_loop:Training step 37 - epoch 36 - loss 4.934456825256348- learning rate 0.0024449999999999993
68 INFO:cray_megatron.megatron.training_loop:Training step 38 - epoch 37 - loss 3.3201217651367188- learning rate 0.0024299999999999994
69 INFO:cray_megatron.megatron.training_loop:Training step 39 - epoch 38 - loss 3.090512990951538- learning rate 0.002414999999999999
70 INFO:cray_megatron.megatron.training_loop:Training step 40 - epoch 39 - loss 2.8569488525390625- learning rate 0.0023999999999999994
71 INFO:cray_megatron.megatron.training_loop:Training step 41 - epoch 40 - loss 2.6222681999206543- learning rate 0.0023849999999999995
72 INFO:cray_megatron.megatron.training_loop:Training step 42 - epoch 41 - loss 2.3898932933807373- learning rate 0.0023699999999999997
73 INFO:cray_megatron.megatron.training_loop:Training step 43 - epoch 42 - loss 2.449845314025879- learning rate 0.0023549999999999995
74 INFO:cray_megatron.megatron.training_loop:Training step 44 - epoch 43 - loss 1.9457842111587524- learning rate 0.0023399999999999996
75 INFO:cray_megatron.megatron.training_loop:Training step 45 - epoch 44 - loss 3.3052239418029785- learning rate 0.002325
76 INFO:cray_megatron.megatron.training_loop:Training step 46 - epoch 45 - loss 1.5511304140090942- learning rate 0.00231
77 INFO:cray_megatron.megatron.training_loop:Training step 47 - epoch 46 - loss 1.381464958190918- learning rate 0.002295
78 INFO:cray_megatron.megatron.training_loop:Training step 48 - epoch 47 - loss 1.8805816173553467- learning rate 0.0022800000000000003
79 INFO:cray_megatron.megatron.training_loop:Training step 49 - epoch 48 - loss 1.6158814430236816- learning rate 0.0022650000000000005
80 INFO:cray_megatron.megatron.training_loop:Training step 50 - epoch 49 - loss 0.9921494722366333- learning rate 0.0022500000000000003
81 INFO:cray_megatron.megatron.training_loop:Training step 51 - epoch 50 - loss 0.9002286791801453- learning rate 0.002235
82 INFO:cray_megatron.megatron.training_loop:Training step 52 - epoch 51 - loss 1.0186548233032227- learning rate 0.00222
83 INFO:cray_megatron.megatron.training_loop:Training step 53 - epoch 52 - loss 0.7658149003982544- learning rate 0.002205
84 INFO:cray_megatron.megatron.training_loop:Training step 54 - epoch 53 - loss 0.7076711654663086- learning rate 0.00219
85 INFO:cray_megatron.megatron.training_loop:Training step 55 - epoch 54 - loss 0.9462921619415283- learning rate 0.002175
86 INFO:cray_megatron.megatron.training_loop:Training step 56 - epoch 55 - loss 0.6228013038635254- learning rate 0.00216
87 INFO:cray_megatron.megatron.training_loop:Training step 57 - epoch 56 - loss 0.5883803367614746- learning rate 0.002145
88 INFO:cray_megatron.megatron.training_loop:Training step 58 - epoch 57 - loss 0.7707682251930237- learning rate 0.0021300000000000004
89 INFO:cray_megatron.megatron.training_loop:Training step 59 - epoch 58 - loss 0.758730411529541- learning rate 0.0021150000000000006
90 INFO:cray_megatron.megatron.training_loop:Training step 60 - epoch 59 - loss 0.506292462348938- learning rate 0.0021000000000000007
91 INFO:cray_megatron.megatron.training_loop:Training step 61 - epoch 60 - loss 0.4830833673477173- learning rate 0.002085000000000001
92 INFO:cray_megatron.megatron.training_loop:Training step 62 - epoch 61 - loss 0.7608119249343872- learning rate 0.002070000000000001
93 INFO:cray_megatron.megatron.training_loop:Training step 63 - epoch 62 - loss 0.43636059761047363- learning rate 0.002055000000000001
94 INFO:cray_megatron.megatron.training_loop:Training step 64 - epoch 63 - loss 0.748888373374939- learning rate 0.002040000000000001
95 INFO:cray_megatron.megatron.training_loop:Training step 65 - epoch 64 - loss 0.3981848359107971- learning rate 0.002025000000000001
96 INFO:cray_megatron.megatron.training_loop:Training step 66 - epoch 65 - loss 0.38111788034439087- learning rate 0.0020100000000000014
97 INFO:cray_megatron.megatron.training_loop:Training step 67 - epoch 66 - loss 0.6918612718582153- learning rate 0.001995000000000001
98 INFO:cray_megatron.megatron.training_loop:Training step 68 - epoch 67 - loss 0.3478345274925232- learning rate 0.001980000000000001
99 INFO:cray_megatron.megatron.training_loop:Training step 69 - epoch 68 - loss 0.7505407333374023- learning rate 0.001965000000000001
100 INFO:cray_megatron.megatron.training_loop:Training step 70 - epoch 69 - loss 0.7745790481567383- learning rate 0.001950000000000001
101 INFO:cray_megatron.megatron.training_loop:Training step 71 - epoch 70 - loss 0.7360649704933167- learning rate 0.001935000000000001
102 INFO:cray_megatron.megatron.training_loop:Training step 72 - epoch 71 - loss 0.6509546637535095- learning rate 0.001920000000000001
103 INFO:cray_megatron.megatron.training_loop:Training step 73 - epoch 72 - loss 0.3059840202331543- learning rate 0.0019050000000000009
104 INFO:cray_megatron.megatron.training_loop:Training step 74 - epoch 73 - loss 0.29385578632354736- learning rate 0.0018900000000000008
105 INFO:cray_megatron.megatron.training_loop:Training step 75 - epoch 74 - loss 0.2902987003326416- learning rate 0.0018750000000000008
106 INFO:cray_megatron.megatron.training_loop:Training step 76 - epoch 75 - loss 0.7161434888839722- learning rate 0.0018600000000000008
107 INFO:cray_megatron.megatron.training_loop:Training step 77 - epoch 76 - loss 0.2615271806716919- learning rate 0.0018450000000000007
108 INFO:cray_megatron.megatron.training_loop:Training step 78 - epoch 77 - loss 0.8070529699325562- learning rate 0.0018300000000000007
109 INFO:cray_megatron.megatron.training_loop:Training step 79 - epoch 78 - loss 0.7276452779769897- learning rate 0.0018150000000000006
110 INFO:cray_megatron.megatron.training_loop:Training step 80 - epoch 79 - loss 0.8069541454315186- learning rate 0.0018000000000000006
111 INFO:cray_megatron.megatron.training_loop:Training step 81 - epoch 80 - loss 0.6734392642974854- learning rate 0.0017850000000000006
112 INFO:cray_megatron.megatron.training_loop:Training step 82 - epoch 81 - loss 0.6499148607254028- learning rate 0.0017700000000000005
113 INFO:cray_megatron.megatron.training_loop:Training step 83 - epoch 82 - loss 0.7235682010650635- learning rate 0.0017550000000000005
114 INFO:cray_megatron.megatron.training_loop:Training step 84 - epoch 83 - loss 0.788324236869812- learning rate 0.0017400000000000004
115 INFO:cray_megatron.megatron.training_loop:Training step 85 - epoch 84 - loss 0.7486412525177002- learning rate 0.0017250000000000004
116 INFO:cray_megatron.megatron.training_loop:Training step 86 - epoch 85 - loss 0.6475511193275452- learning rate 0.0017100000000000006
117 INFO:cray_megatron.megatron.training_loop:Training step 87 - epoch 86 - loss 0.23438769578933716- learning rate 0.0016950000000000005
118 INFO:cray_megatron.megatron.training_loop:Training step 88 - epoch 87 - loss 0.69432532787323- learning rate 0.0016800000000000005
119 INFO:cray_megatron.megatron.training_loop:Training step 89 - epoch 88 - loss 0.701191782951355- learning rate 0.0016650000000000005
120 INFO:cray_megatron.megatron.training_loop:Training step 90 - epoch 89 - loss 0.8208021521568298- learning rate 0.0016500000000000004
121 INFO:cray_megatron.megatron.training_loop:Training step 91 - epoch 90 - loss 0.7423532009124756- learning rate 0.0016350000000000006
122 INFO:cray_megatron.megatron.training_loop:Training step 92 - epoch 91 - loss 0.22764872014522552- learning rate 0.0016200000000000008
123 INFO:cray_megatron.megatron.training_loop:Training step 93 - epoch 92 - loss 0.6770063042640686- learning rate 0.0016050000000000007
124 INFO:cray_megatron.megatron.training_loop:Training step 94 - epoch 93 - loss 0.2195751667022705- learning rate 0.0015900000000000007
125 INFO:cray_megatron.megatron.training_loop:Training step 95 - epoch 94 - loss 0.21528244018554688- learning rate 0.0015750000000000007
126 INFO:cray_megatron.megatron.training_loop:Training step 96 - epoch 95 - loss 0.2105533480644226- learning rate 0.0015600000000000006
127 INFO:cray_megatron.megatron.training_loop:Training step 97 - epoch 96 - loss 0.20401671528816223- learning rate 0.0015450000000000006
128 INFO:cray_megatron.megatron.training_loop:Training step 98 - epoch 97 - loss 0.19684851169586182- learning rate 0.0015300000000000005
129 INFO:cray_megatron.megatron.training_loop:Training step 99 - epoch 98 - loss 0.18342770636081696- learning rate 0.0015150000000000005
130 INFO:cray_megatron.megatron.training_loop:Training step 100 - epoch 99 - loss 0.17346294224262238- learning rate 0.0015000000000000005
131 INFO:cray_infra.training.training_harness:Checkpoint saved to /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/checkpoint_100.pt
132 INFO:cray_infra.training.training_harness:Model saved to /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/saved_model
133 INFO:cray_megatron.megatron.training_loop:Checkpoint on step 100 took 0.748274564743042 seconds
134 INFO:cray_megatron.megatron.training_loop:Training step 101 - epoch 100 - loss 0.16589578986167908- learning rate 0.0014850000000000004
135 INFO:cray_megatron.megatron.training_loop:Training step 102 - epoch 101 - loss 0.7842352986335754- learning rate 0.0014700000000000004
136 INFO:cray_megatron.megatron.training_loop:Training step 103 - epoch 102 - loss 0.8229332566261292- learning rate 0.0014550000000000003
137 INFO:cray_megatron.megatron.training_loop:Training step 104 - epoch 103 - loss 0.749505877494812- learning rate 0.0014400000000000003
138 INFO:cray_megatron.megatron.training_loop:Training step 105 - epoch 104 - loss 0.1399921178817749- learning rate 0.0014250000000000003
139 INFO:cray_megatron.megatron.training_loop:Training step 106 - epoch 105 - loss 0.13615575432777405- learning rate 0.0014100000000000002
140 INFO:cray_megatron.megatron.training_loop:Training step 107 - epoch 106 - loss 0.1328878551721573- learning rate 0.0013950000000000002
141 INFO:cray_megatron.megatron.training_loop:Training step 108 - epoch 107 - loss 0.1299896240234375- learning rate 0.0013800000000000002
142 INFO:cray_megatron.megatron.training_loop:Training step 109 - epoch 108 - loss 0.12737448513507843- learning rate 0.0013650000000000001
143 INFO:cray_megatron.megatron.training_loop:Training step 110 - epoch 109 - loss 0.8569282293319702- learning rate 0.00135
144 INFO:cray_megatron.megatron.training_loop:Training step 111 - epoch 110 - loss 0.8064426183700562- learning rate 0.001335
145 INFO:cray_megatron.megatron.training_loop:Training step 112 - epoch 111 - loss 0.12294523417949677- learning rate 0.00132
146 INFO:cray_megatron.megatron.training_loop:Training step 113 - epoch 112 - loss 0.7471427917480469- learning rate 0.001305
147 INFO:cray_megatron.megatron.training_loop:Training step 114 - epoch 113 - loss 0.12056495994329453- learning rate 0.00129
148 INFO:cray_megatron.megatron.training_loop:Training step 115 - epoch 114 - loss 0.11913363635540009- learning rate 0.0012749999999999999
149 INFO:cray_megatron.megatron.training_loop:Training step 116 - epoch 115 - loss 0.11778314411640167- learning rate 0.0012599999999999998
150 INFO:cray_megatron.megatron.training_loop:Training step 117 - epoch 116 - loss 0.11592821776866913- learning rate 0.0012449999999999998
151 INFO:cray_megatron.megatron.training_loop:Training step 118 - epoch 117 - loss 0.747460126876831- learning rate 0.0012299999999999998
152 INFO:cray_megatron.megatron.training_loop:Training step 119 - epoch 118 - loss 0.11181403696537018- learning rate 0.0012149999999999997
153 INFO:cray_megatron.megatron.training_loop:Training step 120 - epoch 119 - loss 0.11106443405151367- learning rate 0.0011999999999999997
154 INFO:cray_megatron.megatron.training_loop:Training step 121 - epoch 120 - loss 0.7953877449035645- learning rate 0.0011849999999999996
155 INFO:cray_megatron.megatron.training_loop:Training step 122 - epoch 121 - loss 0.7007923126220703- learning rate 0.0011699999999999996
156 INFO:cray_megatron.megatron.training_loop:Training step 123 - epoch 122 - loss 0.5777735710144043- learning rate 0.0011549999999999996
157 INFO:cray_megatron.megatron.training_loop:Training step 124 - epoch 123 - loss 0.10659528523683548- learning rate 0.0011399999999999995
158 INFO:cray_megatron.megatron.training_loop:Training step 125 - epoch 124 - loss 0.6686602830886841- learning rate 0.0011249999999999995
159 INFO:cray_megatron.megatron.training_loop:Training step 126 - epoch 125 - loss 0.7213398218154907- learning rate 0.0011099999999999994
160 INFO:cray_megatron.megatron.training_loop:Training step 127 - epoch 126 - loss 0.10370150953531265- learning rate 0.0010949999999999994
161 INFO:cray_megatron.megatron.training_loop:Training step 128 - epoch 127 - loss 0.715872585773468- learning rate 0.0010799999999999994
162 INFO:cray_megatron.megatron.training_loop:Training step 129 - epoch 128 - loss 0.6672084331512451- learning rate 0.0010649999999999993
163 INFO:cray_megatron.megatron.training_loop:Training step 130 - epoch 129 - loss 0.6094690561294556- learning rate 0.0010499999999999993
164 INFO:cray_megatron.megatron.training_loop:Training step 131 - epoch 130 - loss 0.09981067478656769- learning rate 0.0010349999999999992
165 INFO:cray_megatron.megatron.training_loop:Training step 132 - epoch 131 - loss 0.09831465780735016- learning rate 0.0010199999999999992
166 INFO:cray_megatron.megatron.training_loop:Training step 133 - epoch 132 - loss 0.8732300996780396- learning rate 0.0010049999999999992
167 INFO:cray_megatron.megatron.training_loop:Training step 134 - epoch 133 - loss 0.09659353643655777- learning rate 0.0009899999999999991
168 INFO:cray_megatron.megatron.training_loop:Training step 135 - epoch 134 - loss 0.0957847312092781- learning rate 0.0009749999999999992
169 INFO:cray_megatron.megatron.training_loop:Training step 136 - epoch 135 - loss 0.09486415982246399- learning rate 0.0009599999999999993
170 INFO:cray_megatron.megatron.training_loop:Training step 137 - epoch 136 - loss 0.687118411064148- learning rate 0.0009449999999999992
171 INFO:cray_megatron.megatron.training_loop:Training step 138 - epoch 137 - loss 0.7465814352035522- learning rate 0.0009299999999999993
172 INFO:cray_megatron.megatron.training_loop:Training step 139 - epoch 138 - loss 0.09353536367416382- learning rate 0.0009149999999999994
173 INFO:cray_megatron.megatron.training_loop:Training step 140 - epoch 139 - loss 0.6857355833053589- learning rate 0.0008999999999999993
174 INFO:cray_megatron.megatron.training_loop:Training step 141 - epoch 140 - loss 0.8234232068061829- learning rate 0.0008849999999999993
175 INFO:cray_megatron.megatron.training_loop:Training step 142 - epoch 141 - loss 0.09200795739889145- learning rate 0.0008699999999999994
176 INFO:cray_megatron.megatron.training_loop:Training step 143 - epoch 142 - loss 0.6732250452041626- learning rate 0.0008549999999999993
177 INFO:cray_megatron.megatron.training_loop:Training step 144 - epoch 143 - loss 0.08996626734733582- learning rate 0.0008399999999999993
178 INFO:cray_megatron.megatron.training_loop:Training step 145 - epoch 144 - loss 0.5915161371231079- learning rate 0.0008249999999999992
179 INFO:cray_megatron.megatron.training_loop:Training step 146 - epoch 145 - loss 0.08881303668022156- learning rate 0.0008099999999999992
180 INFO:cray_megatron.megatron.training_loop:Training step 147 - epoch 146 - loss 0.7250931262969971- learning rate 0.0007949999999999993
181 INFO:cray_megatron.megatron.training_loop:Training step 148 - epoch 147 - loss 0.6727677583694458- learning rate 0.0007799999999999993
182 INFO:cray_megatron.megatron.training_loop:Training step 149 - epoch 148 - loss 0.2871503531932831- learning rate 0.0007649999999999993
183 INFO:cray_megatron.megatron.training_loop:Training step 150 - epoch 149 - loss 0.08630774915218353- learning rate 0.0007499999999999993
184 INFO:cray_megatron.megatron.training_loop:Training step 151 - epoch 150 - loss 0.6593747138977051- learning rate 0.0007349999999999992
185 INFO:cray_megatron.megatron.training_loop:Training step 152 - epoch 151 - loss 0.6607116460800171- learning rate 0.0007199999999999992
186 INFO:cray_megatron.megatron.training_loop:Training step 153 - epoch 152 - loss 0.08505091071128845- learning rate 0.0007049999999999991
187 INFO:cray_megatron.megatron.training_loop:Training step 154 - epoch 153 - loss 0.7495298385620117- learning rate 0.0006899999999999991
188 INFO:cray_megatron.megatron.training_loop:Training step 155 - epoch 154 - loss 0.0840618759393692- learning rate 0.0006749999999999992
189 INFO:cray_megatron.megatron.training_loop:Training step 156 - epoch 155 - loss 0.6931415796279907- learning rate 0.0006599999999999991
190 INFO:cray_megatron.megatron.training_loop:Training step 157 - epoch 156 - loss 0.6979023218154907- learning rate 0.0006449999999999992
191 INFO:cray_megatron.megatron.training_loop:Training step 158 - epoch 157 - loss 0.08278802037239075- learning rate 0.0006299999999999992
192 INFO:cray_megatron.megatron.training_loop:Training step 159 - epoch 158 - loss 0.0822552889585495- learning rate 0.0006149999999999991
193 INFO:cray_megatron.megatron.training_loop:Training step 160 - epoch 159 - loss 0.6657384037971497- learning rate 0.0005999999999999991
194 INFO:cray_megatron.megatron.training_loop:Training step 161 - epoch 160 - loss 0.0813547819852829- learning rate 0.000584999999999999
195 INFO:cray_megatron.megatron.training_loop:Training step 162 - epoch 161 - loss 0.6767227649688721- learning rate 0.000569999999999999
196 INFO:cray_megatron.megatron.training_loop:Training step 163 - epoch 162 - loss 0.08070477843284607- learning rate 0.0005549999999999991
197 INFO:cray_megatron.megatron.training_loop:Training step 164 - epoch 163 - loss 0.6971059441566467- learning rate 0.0005399999999999991
198 INFO:cray_megatron.megatron.training_loop:Training step 165 - epoch 164 - loss 0.08001180738210678- learning rate 0.0005249999999999992
199 INFO:cray_megatron.megatron.training_loop:Training step 166 - epoch 165 - loss 0.6862263083457947- learning rate 0.0005099999999999993
200 INFO:cray_megatron.megatron.training_loop:Training step 167 - epoch 166 - loss 0.7431939840316772- learning rate 0.0004949999999999993
201 INFO:cray_megatron.megatron.training_loop:Training step 168 - epoch 167 - loss 0.5616518259048462- learning rate 0.00047999999999999936
202 INFO:cray_megatron.megatron.training_loop:Training step 169 - epoch 168 - loss 0.6773163676261902- learning rate 0.0004649999999999994
203 INFO:cray_megatron.megatron.training_loop:Training step 170 - epoch 169 - loss 0.6207675337791443- learning rate 0.0004499999999999994
204 INFO:cray_megatron.megatron.training_loop:Training step 171 - epoch 170 - loss 0.07802726328372955- learning rate 0.0004349999999999994
205 INFO:cray_megatron.megatron.training_loop:Training step 172 - epoch 171 - loss 0.07783862948417664- learning rate 0.0004199999999999994
206 INFO:cray_megatron.megatron.training_loop:Training step 173 - epoch 172 - loss 0.0776292234659195- learning rate 0.00040499999999999944
207 INFO:cray_megatron.megatron.training_loop:Training step 174 - epoch 173 - loss 0.07749556005001068- learning rate 0.0003899999999999995
208 INFO:cray_megatron.megatron.training_loop:Training step 175 - epoch 174 - loss 0.07696105539798737- learning rate 0.0003749999999999995
209 INFO:cray_megatron.megatron.training_loop:Training step 176 - epoch 175 - loss 0.7952118515968323- learning rate 0.00035999999999999953
210 INFO:cray_megatron.megatron.training_loop:Training step 177 - epoch 176 - loss 0.07636845856904984- learning rate 0.00034499999999999955
211 INFO:cray_megatron.megatron.training_loop:Training step 178 - epoch 177 - loss 0.7084242701530457- learning rate 0.00032999999999999956
212 INFO:cray_megatron.megatron.training_loop:Training step 179 - epoch 178 - loss 0.6410847902297974- learning rate 0.0003149999999999996
213 INFO:cray_megatron.megatron.training_loop:Training step 180 - epoch 179 - loss 0.07575994729995728- learning rate 0.0002999999999999996
214 INFO:cray_megatron.megatron.training_loop:Training step 181 - epoch 180 - loss 0.5927628874778748- learning rate 0.0002849999999999996
215 INFO:cray_megatron.megatron.training_loop:Training step 182 - epoch 181 - loss 0.07534792274236679- learning rate 0.0002699999999999996
216 INFO:cray_megatron.megatron.training_loop:Training step 183 - epoch 182 - loss 0.9427987337112427- learning rate 0.00025499999999999964
217 INFO:cray_megatron.megatron.training_loop:Training step 184 - epoch 183 - loss 0.07497585564851761- learning rate 0.00023999999999999965
218 INFO:cray_megatron.megatron.training_loop:Training step 185 - epoch 184 - loss 0.07496164739131927- learning rate 0.00022499999999999967
219 INFO:cray_megatron.megatron.training_loop:Training step 186 - epoch 185 - loss 0.6813051700592041- learning rate 0.00020999999999999968
220 INFO:cray_megatron.megatron.training_loop:Training step 187 - epoch 186 - loss 0.8017317056655884- learning rate 0.00019499999999999973
221 INFO:cray_megatron.megatron.training_loop:Training step 188 - epoch 187 - loss 0.6315902471542358- learning rate 0.00017999999999999977
222 INFO:cray_megatron.megatron.training_loop:Training step 189 - epoch 188 - loss 0.07442592084407806- learning rate 0.00016499999999999978
223 INFO:cray_megatron.megatron.training_loop:Training step 190 - epoch 189 - loss 0.6251041889190674- learning rate 0.0001499999999999998
224 INFO:cray_megatron.megatron.training_loop:Training step 191 - epoch 190 - loss 0.8014819622039795- learning rate 0.0001349999999999998
225 INFO:cray_megatron.megatron.training_loop:Training step 192 - epoch 191 - loss 0.8565230369567871- learning rate 0.00011999999999999983
226 INFO:cray_megatron.megatron.training_loop:Training step 193 - epoch 192 - loss 0.6923254728317261- learning rate 0.00010499999999999984
227 INFO:cray_megatron.megatron.training_loop:Training step 194 - epoch 193 - loss 0.8134770393371582- learning rate 8.999999999999987e-05
228 INFO:cray_megatron.megatron.training_loop:Training step 195 - epoch 194 - loss 0.8165243864059448- learning rate 7.49999999999999e-05
229 INFO:cray_megatron.megatron.training_loop:Training step 196 - epoch 195 - loss 0.6490029096603394- learning rate 5.999999999999992e-05
230 INFO:cray_megatron.megatron.training_loop:Training step 197 - epoch 196 - loss 0.6595770716667175- learning rate 4.499999999999994e-05
231 INFO:cray_megatron.megatron.training_loop:Training step 198 - epoch 197 - loss 0.07445919513702393- learning rate 2.9999999999999963e-05
232 INFO:cray_megatron.megatron.training_loop:Training step 199 - epoch 198 - loss 0.795946478843689- learning rate 1.4999999999999982e-05
233 INFO:cray_megatron.megatron.training_loop:Training finished successfully after 30.568594932556152 seconds
234 INFO:cray_infra.training.training_harness:Checkpoint saved to /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/checkpoint_199.pt
235 INFO:cray_infra.training.training_harness:Model saved to /app/cray/jobs/69118a251a074f9f9d37a2ddc903243e428d30c3c31ad019cbf62ac777e42e6e/saved_model
```

