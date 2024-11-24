import openhdemg.library as emg
import custom_function as cf

###
emgfile_1 = emg.askopenfile(filesource="OPENHDEMG")
emgfile_2 = emg.askopenfile(filesource="OPENHDEMG")


custom_sorting_order_TMSi_4_8_L = [
    [31, 30, 29, 28, 27, 26, 25, 24],
    [23, 22, 21, 20, 19, 18, 17, 16],
    [15, 14, 13, 12, 11, 10,  9,  8],
    [ 7,  6,  5,  4,  3,  2,  1,  0],
]

'''
custom_sorting_order_TMSi_4_8_L = [
    [31[R4C8], 30[R4C7], 29[R4C6], 28[R4C5], 27[R4C4], 26[R4C3], 25[R4C2], 24[R4C1]],
    [23[R3C8], 22[R3C7], 21[R3C6], 20[R3C5], 19[R3C4], 18[R3C3], 17[R3C2], 16[R3C1]],
    [ 15[R2C8],  14[R2C7], 13[R2C6], 12[R2C5], 11[R2C4], 10[R2C3], 9[R2C2], 8[R2C1]],
    [  7[R1C8],  6[R1C7],  5[R1C6],  4[R1C5],  3[R1C4],  2[R1C3],  1[R1C2],  0[R1C1]],
]
'''

tracking_res = emg.tracking(
    emgfile_1,
    emgfile_2,
    firings="all",
    derivation="sd",
    timewindow=50,
    threshold=0.7,
    matrixcode="Custom order",
    custom_sorting_order=custom_sorting_order_TMSi_4_8_L,
    orientation=180,
    filter=True,
    show=True,
    gui=True
)

cf.save_dataframe_as_csv(tracking_res, include_index=True)
