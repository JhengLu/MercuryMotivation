import re
import numpy as np

# Sample data
data = """

TIME 2024-01-08 15:30:31
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.99     240787k     37800.0     16703.5      1476.5
TIME 2024-01-08 15:30:32
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.92     245459k     42000.0     16970.7      2446.6
TIME 2024-01-08 15:30:33
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.03     239775k     39312.0     16928.4       964.3
TIME 2024-01-08 15:30:34
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.92     243675k     40096.0     16785.0      1932.4
TIME 2024-01-08 15:30:35
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.01     243563k     37128.0     17074.2       789.9
TIME 2024-01-08 15:30:36
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     244537k     39256.0     17044.6      1143.9
TIME 2024-01-08 15:30:37
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.94     243988k     40040.0     16984.2      1072.8
TIME 2024-01-08 15:30:38
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     238022k     39872.0     16680.3       994.4
TIME 2024-01-08 15:30:39
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     239262k     42560.0     16647.7      1275.1
TIME 2024-01-08 15:30:40
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.95     239523k     38304.0     16605.3      1577.1
TIME 2024-01-08 15:30:41
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     236958k     39144.0     16379.6      1432.4
TIME 2024-01-08 15:30:42
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.02     240447k     40824.0     16758.3      1027.9
TIME 2024-01-08 15:30:43
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     234469k     42392.0     16297.9      1505.4
TIME 2024-01-08 15:30:44
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     241929k     42616.0     16910.1      1273.6
TIME 2024-01-08 15:30:45
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.92     244136k     39312.0     16955.1      1231.0
TIME 2024-01-08 15:30:46
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     240503k     39984.0     16697.1      1281.3
TIME 2024-01-08 15:30:47
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.95     241038k     40264.0     16540.7      1421.4
TIME 2024-01-08 15:30:48
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.02     235773k     39760.0     16426.2       991.3
TIME 2024-01-08 15:30:49
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.94     247294k     42784.0     17114.3      1266.6
TIME 2024-01-08 15:30:50
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.00     236166k     40208.0     16482.6      1251.5
TIME 2024-01-08 15:30:51
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.00     240050k     40432.0     16718.5      1477.9
TIME 2024-01-08 15:30:52
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     239530k     39480.0     16697.4      1208.5
TIME 2024-01-08 15:30:53
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.01     240626k     41160.0     16818.3      1623.3
TIME 2024-01-08 15:30:54
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.95     244089k     41104.0     16817.6      1319.2
TIME 2024-01-08 15:30:55
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.96     243120k     40152.0     16842.8      1294.3
TIME 2024-01-08 15:30:56
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.94     243615k     42728.0     16922.7      1324.5
TIME 2024-01-08 15:30:57
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.95     245246k     42840.0     16847.1      1308.7
TIME 2024-01-08 15:30:58
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.96     239797k     42056.0     16540.5      1216.4
TIME 2024-01-08 15:30:59
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.92     240055k     42504.0     16638.3      1265.0
TIME 2024-01-08 15:31:00
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     243633k     42056.0     16799.0      1457.7
TIME 2024-01-08 15:31:01
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.98     238910k     39928.0     16743.8      1278.4
TIME 2024-01-08 15:31:02
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.95     241476k     39032.0     16851.3      1105.2
TIME 2024-01-08 15:31:03
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.99     241918k     42672.0     16845.3      1249.7
TIME 2024-01-08 15:31:04
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.99     237792k     40208.0     16560.7      1066.7
TIME 2024-01-08 15:31:05
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.94     242113k     38752.0     16768.0      1976.9
TIME 2024-01-08 15:31:06
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.04     237165k     39256.0     16619.0      1068.2
TIME 2024-01-08 15:31:07
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     237374k     39760.0     16519.9      1034.4
TIME 2024-01-08 15:31:08
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     240524k     42896.0     16728.2      1508.2
TIME 2024-01-08 15:31:09
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.93     244524k     39144.0     16854.8      1645.4
TIME 2024-01-08 15:31:10
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.97     242363k     39648.0     16874.2      1268.4
TIME 2024-01-08 15:31:11
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.93     242291k     39760.0     16773.0      2216.3
TIME 2024-01-08 15:31:12
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.02     238287k     39312.0     16612.3      1045.2
TIME 2024-01-08 15:31:13
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.99     242463k     38752.0     16831.7      1047.8
TIME 2024-01-08 15:31:14
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.02     240587k     42112.0     16891.8      1142.6
TIME 2024-01-08 15:31:15
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.88     245711k     40040.0     16907.7      1802.8
TIME 2024-01-08 15:31:16
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        2.01     236190k     39312.0     16455.6      1417.1
TIME 2024-01-08 15:31:17
    CORE         IPC      MISSES     LLC[KB]   MBL[MB/s]   MBR[MB/s]
0-27,56-        1.94     245833k     39928.0     17003.9      1339.8





"""

# Regular expression to extract the MBL[MB/s] data
mbl_pattern = re.compile(r"0-27,56-.*?\s+[\d.]+\s+[\d.]+k+\s+[\d.]+\s+([\d.]+)+\s+[\d.]+")


# Extracting the MBL values
mbl_values = [float(match) for match in mbl_pattern.findall(data)]

# Calculating the median
median_mbl = np.median(mbl_values)
print(median_mbl)

