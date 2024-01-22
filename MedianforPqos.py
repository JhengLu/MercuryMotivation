import re
import numpy as np

# Sample data
data = """

TIME 2024-01-15 14:10:13
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78     871930k     42560.0     92951.4         5.4
TIME 2024-01-15 14:10:14
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.23     679070k     42224.0     69870.4         5.6
TIME 2024-01-15 14:10:15
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.85    1098344k     42672.0     83233.2        10.1
TIME 2024-01-15 14:10:16
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1291610k     42560.0     92339.4         8.1
TIME 2024-01-15 14:10:17
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1278894k     42840.0     89431.3         7.8
TIME 2024-01-15 14:10:18
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1247285k     42504.0     85687.8         8.6
TIME 2024-01-15 14:10:19
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.84    1088771k     42336.0     74919.7         6.6
TIME 2024-01-15 14:10:20
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1262770k     42616.0     87078.3         8.1
TIME 2024-01-15 14:10:21
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1254812k     42280.0     86582.6         7.7
TIME 2024-01-15 14:10:22
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.63    1233356k     42504.0     84495.9         8.3
TIME 2024-01-15 14:10:23
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.82     984031k     42504.0     66275.2         7.1
TIME 2024-01-15 14:10:24
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1242363k     42728.0     85177.1         5.8
TIME 2024-01-15 14:10:25
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1247836k     42728.0     85710.1        10.1
TIME 2024-01-15 14:10:26
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.69    1163342k     42952.0     79669.4         9.4
TIME 2024-01-15 14:10:27
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.79    1142222k     42616.0     78246.9         8.0
TIME 2024-01-15 14:10:28
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1248251k     42224.0     85631.5         8.8
TIME 2024-01-15 14:10:29
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78    1092272k     42728.0     74996.5         4.9
TIME 2024-01-15 14:10:30
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70    1202487k     42560.0     82749.8        10.0
TIME 2024-01-15 14:10:31
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.76    1106643k     42840.0     76069.4         8.1
TIME 2024-01-15 14:10:32
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.69    1200580k     42616.0     82692.8         7.9
TIME 2024-01-15 14:10:33
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.80    1066653k     42616.0     73631.4         6.2
TIME 2024-01-15 14:10:34
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.77    1098252k     42616.0     75804.7         7.3
TIME 2024-01-15 14:10:35
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78    1084180k     42560.0     74667.4         8.6
TIME 2024-01-15 14:10:36
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.82    1039941k     42392.0     71496.6         9.2
TIME 2024-01-15 14:10:37
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.95     874508k     42840.0     60264.6         7.2
TIME 2024-01-15 14:10:38
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78     840388k     42112.0     63271.3         4.3
TIME 2024-01-15 14:10:39
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904281k     41944.0     67871.0        10.4
TIME 2024-01-15 14:10:40
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904879k     42000.0     67864.8        11.6
TIME 2024-01-15 14:10:41
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     902758k     42000.0     67582.3         8.4
TIME 2024-01-15 14:10:42
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     902698k     42056.0     67665.4        10.0
TIME 2024-01-15 14:10:43
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     902491k     42280.0     67534.1         9.4
TIME 2024-01-15 14:10:44
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900387k     42168.0     67375.9         8.6
TIME 2024-01-15 14:10:45
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898405k     42224.0     67257.0         8.8
TIME 2024-01-15 14:10:46
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     901041k     42112.0     67381.8        14.5
TIME 2024-01-15 14:10:47
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900299k     41328.0     67310.2        10.8
TIME 2024-01-15 14:10:48
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899948k     42000.0     67217.0         8.2
TIME 2024-01-15 14:10:49
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898649k     42056.0     67217.4        10.6
TIME 2024-01-15 14:10:50
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898969k     42336.0     67179.7        10.3
TIME 2024-01-15 14:10:51
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898684k     42224.0     67099.6        10.2
TIME 2024-01-15 14:10:52
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897671k     42392.0     67050.2         8.8
TIME 2024-01-15 14:10:53
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     899807k     42056.0     67175.6         9.8
TIME 2024-01-15 14:10:54
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897878k     42168.0     66977.8         8.4
TIME 2024-01-15 14:10:55
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898730k     42336.0     67089.1         9.2
TIME 2024-01-15 14:10:56
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897152k     42560.0     66929.4        10.2
TIME 2024-01-15 14:10:57
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898246k     42168.0     67039.3         9.5
TIME 2024-01-15 14:10:58
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898997k     42336.0     67027.4         9.5
TIME 2024-01-15 14:10:59
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898689k     42560.0     67047.4        10.6
TIME 2024-01-15 14:11:00
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.94     650672k     42728.0     47184.8         7.4
TIME 2024-01-15 14:11:01
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.86     887084k     42448.0     59887.7         7.3
TIME 2024-01-15 14:11:02
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.10    1282118k     42840.0     84282.1         6.6
TIME 2024-01-15 14:11:03
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.86    1091513k     42448.0     82723.4         6.5
TIME 2024-01-15 14:11:04
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1289259k     42672.0     92165.4         6.2
TIME 2024-01-15 14:11:05
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1277602k     42784.0     89338.2         6.0
TIME 2024-01-15 14:11:06
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1252157k     41888.0     86071.5         8.4
TIME 2024-01-15 14:11:07
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.84    1073531k     42504.0     73917.9         6.8
TIME 2024-01-15 14:11:08
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1255249k     42224.0     86554.7         6.9
TIME 2024-01-15 14:11:09
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1250286k     42448.0     86327.4         9.0
TIME 2024-01-15 14:11:10
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.63    1230391k     42672.0     84342.6         7.4
TIME 2024-01-15 14:11:11
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.82     980238k     42448.0     66095.9         5.4
TIME 2024-01-15 14:11:12
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1220018k     42840.0     83706.9        12.5
TIME 2024-01-15 14:11:13
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1228918k     42336.0     84464.2         9.6
TIME 2024-01-15 14:11:14
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1225982k     42896.0     84010.8         6.6
TIME 2024-01-15 14:11:15
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.83    1074289k     42112.0     73581.6         8.5
TIME 2024-01-15 14:11:16
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1246150k     42504.0     85664.6         9.2
TIME 2024-01-15 14:11:17
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.74    1121759k     42616.0     76965.7         7.7
TIME 2024-01-15 14:11:18
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71    1199711k     42784.0     82443.5         8.7
TIME 2024-01-15 14:11:19
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.73    1137658k     42896.0     78227.6         8.8
TIME 2024-01-15 14:11:20
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.72    1176711k     42616.0     80999.8        13.5
TIME 2024-01-15 14:11:21
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1067715k     42840.0     73565.1         9.6
TIME 2024-01-15 14:11:22
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.76    1100857k     42336.0     75851.8         8.1
TIME 2024-01-15 14:11:23
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.79    1075809k     42504.0     74094.9         7.3
TIME 2024-01-15 14:11:24
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.83    1041806k     42560.0     71592.6        10.2
TIME 2024-01-15 14:11:25
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.95     873017k     42392.0     60317.5         9.9
TIME 2024-01-15 14:11:26
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.76     856779k     42336.0     64434.2        10.2
TIME 2024-01-15 14:11:27
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     906205k     42224.0     67990.3         8.2
TIME 2024-01-15 14:11:28
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904587k     41944.0     67801.0         9.4
TIME 2024-01-15 14:11:29
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     903062k     42336.0     67617.3         9.0
TIME 2024-01-15 14:11:30
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     903374k     41720.0     67710.0         7.4
TIME 2024-01-15 14:11:31
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900309k     42168.0     67350.0         9.5
TIME 2024-01-15 14:11:32
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900578k     42112.0     67395.7         9.0
TIME 2024-01-15 14:11:33
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900445k     41776.0     67453.9         8.9
TIME 2024-01-15 14:11:34
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     901877k     42336.0     67471.0         8.7
TIME 2024-01-15 14:11:35
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900541k     41608.0     67248.2         7.4
TIME 2024-01-15 14:11:36
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899813k     42280.0     67166.4         7.8
TIME 2024-01-15 14:11:37
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899525k     41944.0     67225.3         9.4
TIME 2024-01-15 14:11:38
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898108k     42000.0     67127.2         7.9
TIME 2024-01-15 14:11:39
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899961k     42000.0     67192.6         8.3
TIME 2024-01-15 14:11:40
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899170k     42000.0     67095.6         8.9
TIME 2024-01-15 14:11:41
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899373k     41888.0     67162.6         8.6
TIME 2024-01-15 14:11:42
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897234k     42392.0     66938.9         9.7
TIME 2024-01-15 14:11:43
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897678k     41944.0     66990.0         9.2
TIME 2024-01-15 14:11:44
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     887078k     42504.0     66211.6        12.2
TIME 2024-01-15 14:11:45
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     896567k     41944.0     66877.8        11.8
TIME 2024-01-15 14:11:46
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     895077k     42112.0     66727.8        13.2
TIME 2024-01-15 14:11:47
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     895572k     42280.0     66838.3        10.8
TIME 2024-01-15 14:11:48
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.94     671104k     43008.0     48323.6         7.9
TIME 2024-01-15 14:11:49
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.86     869804k     42112.0     58810.6        11.8
TIME 2024-01-15 14:11:50
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.18    1277172k     42952.0     80473.8         6.6
TIME 2024-01-15 14:11:51
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.99     682983k     42896.0     41810.0         0.7
TIME 2024-01-15 14:11:52
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.92     618653k     42784.0     37805.5         2.2
TIME 2024-01-15 14:11:53
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.36     830650k     42448.0     62337.2         7.3
TIME 2024-01-15 14:11:54
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1270350k     42504.0     92197.6         7.4
TIME 2024-01-15 14:11:55
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1145344k     42728.0     81530.9         8.8
TIME 2024-01-15 14:11:56
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1280660k     42560.0     90475.3         6.9
TIME 2024-01-15 14:11:57
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1268169k     42784.0     88409.4         6.8
TIME 2024-01-15 14:11:58
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.62    1233879k     42560.0     84516.0         8.5
TIME 2024-01-15 14:11:59
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81     986643k     42616.0     66533.6         6.7
TIME 2024-01-15 14:12:00
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1241511k     42224.0     84956.2        10.8
TIME 2024-01-15 14:12:01
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1244466k     42672.0     85139.0        12.0
TIME 2024-01-15 14:12:02
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1237327k     42672.0     84583.0         8.0
TIME 2024-01-15 14:12:03
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.82    1016949k     42840.0     68872.1         7.7
TIME 2024-01-15 14:12:04
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1238049k     42840.0     84576.1         7.5
TIME 2024-01-15 14:12:05
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1246573k     42448.0     85401.9         8.8
TIME 2024-01-15 14:12:06
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1074121k     42784.0     73882.6         6.5
TIME 2024-01-15 14:12:07
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1241546k     42672.0     85469.1         7.2
TIME 2024-01-15 14:12:08
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1069719k     42448.0     73814.2         6.9
TIME 2024-01-15 14:12:09
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.75    1115709k     42672.0     76975.0         6.3
TIME 2024-01-15 14:12:10
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1205691k     42840.0     83114.2         7.7
TIME 2024-01-15 14:12:11
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.79    1085352k     42672.0     74760.6         6.3
TIME 2024-01-15 14:12:12
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78    1093877k     42392.0     75451.0         7.5
TIME 2024-01-15 14:12:13
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.86     995327k     42840.0     68499.5         4.9
TIME 2024-01-15 14:12:14
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.94     907921k     42784.0     62524.7         6.2
TIME 2024-01-15 14:12:15
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.84     831181k     42000.0     61291.7         6.7
TIME 2024-01-15 14:12:16
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904711k     41888.0     67894.8         8.5
TIME 2024-01-15 14:12:17
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904269k     42168.0     67877.6         7.2
TIME 2024-01-15 14:12:18
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     902976k     42000.0     67714.8         9.8
TIME 2024-01-15 14:12:19
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     902006k     42112.0     67561.6         8.8
TIME 2024-01-15 14:12:20
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     896409k     42336.0     67143.3         7.9
TIME 2024-01-15 14:12:21
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     894396k     42504.0     67001.7         7.4
TIME 2024-01-15 14:12:22
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900427k     42112.0     67440.7        10.1
TIME 2024-01-15 14:12:23
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     894259k     42336.0     67033.8         9.2
TIME 2024-01-15 14:12:24
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898362k     42504.0     67246.3         8.5
TIME 2024-01-15 14:12:25
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     896734k     42168.0     67098.0        13.5
TIME 2024-01-15 14:12:26
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     874465k     41664.0     65275.4        13.7
TIME 2024-01-15 14:12:27
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     894641k     41888.0     66916.1         8.9
TIME 2024-01-15 14:12:28
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     892198k     42224.0     66683.0        12.1
TIME 2024-01-15 14:12:29
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898392k     42112.0     67124.6        10.6
TIME 2024-01-15 14:12:30
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897664k     42056.0     67104.5         9.2
TIME 2024-01-15 14:12:31
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     891623k     41888.0     66637.2        10.7
TIME 2024-01-15 14:12:32
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     896862k     42336.0     67040.5        11.9
TIME 2024-01-15 14:12:33
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897487k     42280.0     66992.9        14.7
TIME 2024-01-15 14:12:34
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     895202k     41944.0     66795.6        13.9
TIME 2024-01-15 14:12:35
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     896703k     42168.0     66880.9        11.2
TIME 2024-01-15 14:12:36
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     894000k     42392.0     66679.5        13.6
TIME 2024-01-15 14:12:37
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.75     867529k     41776.0     64736.3        13.6
TIME 2024-01-15 14:12:38
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.95     704049k     42672.0     47966.2         8.7
TIME 2024-01-15 14:12:39
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.02    1148828k     43008.0     73285.6         7.8
TIME 2024-01-15 14:12:40
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.19     904289k     42728.0     55513.0         0.5
TIME 2024-01-15 14:12:41
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.83     566341k     43008.0     34617.9         1.6
TIME 2024-01-15 14:12:42
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.47     729861k     42504.0     51553.6         3.9
TIME 2024-01-15 14:12:43
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.83    1121945k     42000.0     82495.3         7.9
TIME 2024-01-15 14:12:44
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1287546k     42448.0     91932.5         6.3
TIME 2024-01-15 14:12:45
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1282545k     42448.0     89704.1         5.4
TIME 2024-01-15 14:12:46
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1265604k     42392.0     87129.3         6.7
TIME 2024-01-15 14:12:47
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.83    1081733k     42672.0     74264.1         6.2
TIME 2024-01-15 14:12:48
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1263223k     42560.0     87162.6         6.3
TIME 2024-01-15 14:12:49
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1263099k     42560.0     87170.7         7.4
TIME 2024-01-15 14:12:50
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1245767k     42168.0     85476.6         7.6
TIME 2024-01-15 14:12:51
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.84     995430k     42448.0     67568.8         6.7
TIME 2024-01-15 14:12:52
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1253680k     42392.0     85835.3         8.4
TIME 2024-01-15 14:12:53
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1253712k     42616.0     85949.9         7.3
TIME 2024-01-15 14:12:54
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1193337k     42112.0     81630.9         8.5
TIME 2024-01-15 14:12:55
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1104643k     42280.0     75473.7         7.8
TIME 2024-01-15 14:12:56
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1247931k     42728.0     85478.3         7.9
TIME 2024-01-15 14:12:57
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1079063k     42616.0     74010.2         6.9
TIME 2024-01-15 14:12:58
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1209321k     42616.0     83299.6         7.4
TIME 2024-01-15 14:12:59
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78    1115054k     42280.0     76945.2         8.4
TIME 2024-01-15 14:13:00
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.80    1092691k     42728.0     75400.2         7.1
TIME 2024-01-15 14:13:01
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.80    1085414k     42448.0     74763.0         7.7
TIME 2024-01-15 14:13:02
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.89     972726k     42728.0     67015.6         9.5
TIME 2024-01-15 14:13:03
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.97     873443k     42448.0     60234.0         6.9
TIME 2024-01-15 14:13:04
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.84     827667k     42504.0     60904.9         8.5
TIME 2024-01-15 14:13:05
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897843k     41720.0     67377.5         7.4
TIME 2024-01-15 14:13:06
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     904565k     42000.0     67879.6        13.2
TIME 2024-01-15 14:13:07
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     905660k     41216.0     67849.9        10.0
TIME 2024-01-15 14:13:08
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     904289k     42000.0     67760.9         9.6
TIME 2024-01-15 14:13:09
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900444k     41944.0     67407.9         8.4
TIME 2024-01-15 14:13:10
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900192k     42224.0     67357.9        11.0
TIME 2024-01-15 14:13:11
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898876k     42392.0     67354.3         7.8
TIME 2024-01-15 14:13:12
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900418k     41776.0     67398.8         9.8
TIME 2024-01-15 14:13:13
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900908k     41944.0     67354.1        15.0
TIME 2024-01-15 14:13:14
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     902549k     42056.0     67461.7         8.9
TIME 2024-01-15 14:13:15
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     900279k     41832.0     67300.9        11.2
TIME 2024-01-15 14:13:16
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899485k     41776.0     67220.5         7.9
TIME 2024-01-15 14:13:17
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899947k     42336.0     67210.9        13.5
TIME 2024-01-15 14:13:18
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897616k     42168.0     67012.1         9.2
TIME 2024-01-15 14:13:19
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899316k     42280.0     67171.5         8.5
TIME 2024-01-15 14:13:20
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899604k     42000.0     67116.1         8.8
TIME 2024-01-15 14:13:21
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     897958k     42392.0     67052.8        10.1
TIME 2024-01-15 14:13:22
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.70     900376k     42392.0     67188.9        10.6
TIME 2024-01-15 14:13:23
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     898120k     42392.0     66971.6         9.0
TIME 2024-01-15 14:13:24
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899703k     41944.0     67033.4        11.4
TIME 2024-01-15 14:13:25
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.71     899269k     42392.0     67011.4         7.8
TIME 2024-01-15 14:13:26
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.98     638233k     42784.0     45501.7         6.2
TIME 2024-01-15 14:13:27
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78     913070k     42224.0     64948.5         7.9
TIME 2024-01-15 14:13:28
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.88     909766k     42840.0     59425.1         5.8
TIME 2024-01-15 14:13:29
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.30    1248557k     42896.0     77830.0         3.9
TIME 2024-01-15 14:13:30
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.85     577865k     42896.0     35375.5         1.0
TIME 2024-01-15 14:13:31
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.24     698023k     42952.0     42653.4         1.2
TIME 2024-01-15 14:13:32
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        1.02    1038443k     42784.0     80623.2         8.1
TIME 2024-01-15 14:13:33
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1290098k     42784.0     92243.0         7.4
TIME 2024-01-15 14:13:34
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.82    1125911k     42616.0     79023.7         9.1
TIME 2024-01-15 14:13:35
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1271523k     42448.0     89178.4         6.8
TIME 2024-01-15 14:13:36
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1270245k     42392.0     88640.3         6.6
TIME 2024-01-15 14:13:37
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.63    1239244k     42616.0     85157.2         8.6
TIME 2024-01-15 14:13:38
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.78     966446k     42784.0     64880.3         5.9
TIME 2024-01-15 14:13:39
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.69    1214002k     42560.0     82978.7        11.0
TIME 2024-01-15 14:13:40
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1222282k     42728.0     83773.4         9.1
TIME 2024-01-15 14:13:41
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1239243k     42616.0     84903.8         8.0
TIME 2024-01-15 14:13:42
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.80    1048466k     42784.0     71547.5         8.7
TIME 2024-01-15 14:13:43
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.67    1242755k     42504.0     85150.6         9.5
TIME 2024-01-15 14:13:44
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.64    1252016k     42392.0     86130.2        10.9
TIME 2024-01-15 14:13:45
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.80    1085325k     42560.0     74539.2         6.9
TIME 2024-01-15 14:13:46
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.66    1240480k     42672.0     85265.7        11.4
TIME 2024-01-15 14:13:47
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.65    1227162k     42672.0     84447.9         8.8
TIME 2024-01-15 14:13:48
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.81    1079222k     42616.0     74251.2        12.8
TIME 2024-01-15 14:13:49
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.68    1191727k     42504.0     82002.3         9.0
TIME 2024-01-15 14:13:50
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.76    1124675k     42224.0     77668.9         8.0
TIME 2024-01-15 14:13:51
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.79    1079376k     42336.0     74480.7         6.6
TIME 2024-01-15 14:13:52
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.72    1150015k     42000.0     79329.3        10.2
TIME 2024-01-15 14:13:53
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.77    1103498k     42504.0     76128.8        12.7
TIME 2024-01-15 14:13:54
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.85    1018779k     42784.0     70272.8        10.1
TIME 2024-01-15 14:13:55
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
28-55,84        0.85    1029948k     42728.0     71084.5         6.8





"""

# Regular expression to extract the MBL[MB/s] data
mbl_pattern = re.compile(r"28-55,84.*?\s+[\d.]+\s+[\d.]+k+\s+[\d.]+\s+([\d.]+)+\s+[\d.]+")


# Extracting the MBL values
mbl_values = [float(match) for match in mbl_pattern.findall(data)]

# Calculating the median
median_mbl = np.median(mbl_values)
print("median: " + str(median_mbl))

# Calculate the average of MBL values
average_mbl = np.mean(mbl_values)

print(f"Average MBL: {average_mbl} MB/s")

