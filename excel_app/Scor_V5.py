from tkinter import Tk
from tkinter import Canvas
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import filedialog
from tkinter import messagebox
import datetime
import pandas as pd
import os
from .models import SayimRapor

def rapor_calistir_(ham_veri, sorgu_list_, sorgu_ref_, saha_no, rapor):

    df = pd.DataFrame()
    data_fix = pd.DataFrame()
    basla = pd.DataFrame()
    girdiler = []
    # Excel okuma ile Analiz satırlarını birleştiriyoruz. 1. Bölüm Excel Okuma ve Değişkenleri alma
    data = ham_veri

#     Analiz_1 = [106, 109, 110, 118, 147, 186, 212]
#     Analiz_2 = [184, 185, 187]
#     Analiz_3 = [111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 126, 127, 128, 129, 130, 138, 145, 148, 149, 150, 151, 152, 153, 154, 156, 157, 160, 161, 163, 165, 215, 225, 237, 245, 248, 273, 321, 350, 422]
#     Analiz_4 = [131, 132, 133, 134, 135]
#     Analiz_5 = [144, 164, 166, 168, 238]
#     Analiz_6 = [169, 170, 171, 172, 173, 174]
#     Analiz_7 = [123]
#     Analiz_8 = [158, 159, 175, 176, 177, 271]
#     Analiz_9 = [136]
#     Analiz_10 = [178]
#     Analiz_11 = [139]
#     Analiz_12 = [179, 424]
#     Analiz_13 = [180]
#     Analiz_14 = [146]
#     Analiz_15 = [181]
#     Analiz_16 = [182]
#     Analiz_17 = [101]
#     Analiz_18 = [102, 105, 141, 183, 188, 189, 190, 191, 192, 193, 194, 195, 200, 201, 202, 203, 204, 207, 208, 210, 211, 230,
#                  233, 234, 235, 236, 239, 240, 241, 242, 243, 244, 270, 272, 300, 301, 302, 303, 351, 354, 357, 420,
#                  423, 425, 426, 427, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442]
#     Analiz_19 = [137]
#     Analiz_20 = [107]
#     Analiz_21 = [197]
#     Analiz_22 = [199]
#     Analiz_23 = [198]
#     Analiz_24 = [214]
#     Analiz_25 = [155, 213]
#     Analiz_26 = [104, 196]
# #    Analiz_27 = [191]
#     Analiz_28 = [219]
#     Analiz_29 = [212]
#     Analiz_30 = [223]
#     Analiz_31 = [421]
#     Analiz_32 = [143]
#     Analiz_33 = [226]
#     Analiz_34 = [209, 400, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413]
#     Analiz_35 = [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298]
#     Analiz_36 = [108]
#     Analiz_37 = [305, 306, 307, 308, 309]
#     Analiz_38 = [310]
#     Analiz_39 = [218]
#     Analiz_40 = [140]
#     Analiz_41 = [205]
#     Analiz_42 = [124]
#     Analiz_43 = [142]
#     Analiz_44 = [216, 217]
# #    Analiz_45 = [210]
#     Analiz_46 = [162]

    sorgu_ref = sorgu_ref_
    sorgu_list = sorgu_list_
    is_sayim_sonrasi_envanter = False
    for col in data.columns:

        if "Saha No" == col:
            data_fix = pd.DataFrame(data[['Saha No', 'Saha Kodu', 'Ekipman Parca Kodu', 'Parca Tanimi', 'Quantity']])
            break
        
        elif "sayim" == col:
            
            is_sayim_sonrasi_envanter = True
            break
        
        elif "Kullanıcı" == col:
            data_fix = pd.DataFrame(data[['Lokasyon Kodu', 'Kullanıcı', 'Kalem Kodu', 'Kalem Tanımı', 'Miktar', 'Sayım Fark', 'Transfer Edilen Adet', 'Zimmet Departmani']])
            data_fix = data_fix.rename(columns={'Lokasyon Kodu': 'Saha No', 'Kullanıcı': 'Saha Kodu', 'Kalem Kodu': 'Ekipman Parca Kodu', 'Kalem Tanımı': 'Parca Tanimi', 'Miktar': 'Quantity'}, inplace=False)
            break
        elif "Kullanici" == col:
            data_fix = pd.DataFrame(data[['Lokasyon Kodu', 'Kullanici', 'Kalem Kodu', 'Kalem Tanimi', 'Miktar', 'Sayim Fark', 'Transfer Edilen Adet', 'Zimmet Departmani']])
            data_fix = data_fix.rename(columns={'Lokasyon Kodu': 'Saha No', 'Kullanici': 'Saha Kodu', 'Kalem Kodu': 'Ekipman Parca Kodu', 'Kalem Tanimi': 'Parca Tanimi', 'Miktar': 'Quantity'}, inplace=False)
            break
        elif "Saha Varlık No" == col:
            data_fix = pd.DataFrame(data[['Saha Kodu', 'Saha Varlık No', 'Kalem Kodu', 'Kalem Tanımı', 'Miktar']])
            data_fix = data_fix.rename(columns={'Lokasyon Kodu': 'Saha No', 'Saha Varlık No': 'Saha Kodu', 'Kalem Kodu': 'Ekipman Parca Kodu', 'Kalem Tanımı': 'Parca Tanimi', 'Miktar': 'Quantity'}, inplace=False)
            break

    basla = data_fix.drop_duplicates(subset=["Saha No", "Saha Kodu"]).reset_index()

    for h in basla.index[0:]:
        # Envanter dosyasında saha_no ve ID bilgileri alınır
        Saha_Nox = (basla.iloc[h, 1])
        Saha_Kodu = (basla.iloc[h, 2])

        data_fix_1 = pd.DataFrame(data_fix[data_fix['Saha No'] == Saha_Nox])

        for i in sorgu_list.index[0:]:
            Sorgu_Nox = (sorgu_list.iloc[i, 0])
            Kontrol = (sorgu_list.iloc[i, 1])
            Ref_Grup = (sorgu_list.iloc[i, 2])
            Kategori = (sorgu_list.iloc[i, 3])
            Check = (sorgu_list.iloc[i, 4])

        # Referans listesinde ki sorgu satırları tabloya alınır
            sorgu_fix_1 = pd.DataFrame(sorgu_ref[sorgu_ref['Sorgu_No'] == Sorgu_Nox])

    # Envanter ile Referans sorgu tabloları birleştirilir.
            grupby_data = (pd.merge(data_fix_1, sorgu_fix_1, how="inner"))

    # Birleştirilen tabloları da ki referans parç kodlarına göre malzeme toplamları yapılır.
            Ref_Kon = grupby_data.groupby(by=['Ref']).sum()['Quantity'].reset_index()

            Ref_1 = 0
            Ref_2 = 0
            Ref_3 = 0
            Ref_4 = 0
            Ref_5 = 0
            Ref_6 = 0
            Ref_01 = 0
            Ref_02 = 0
            Ref_03 = 0
            Bilgi = ""
            Sonuc = "Kontrol"

        # Birleştirilen tabloda ki genel toplamaların Referans ve toplamların değerleri ayrıştırılır.
            for z in Ref_Kon.index[0:]:
                Ref_x = (Ref_Kon.iloc[z, 0])
                Ref_y = (Ref_Kon.iloc[z, 1])
        # Çıktıda ki Referans bilgileri hangi referanslara yazılacağı tespit edilir.
                if Ref_x == 'Ref_1':
                    Ref_1 = Ref_y
                elif Ref_x == 'Ref_2':
                    Ref_2 = Ref_y
                elif Ref_x == 'Ref_3':
                    Ref_3 = Ref_y
                elif Ref_x == 'Ref_4':
                    Ref_4 = Ref_y
                elif Ref_x == 'Ref_5':
                    Ref_5 = Ref_y
                elif Ref_x == 'Ref_6':
                    Ref_6 = Ref_y
                elif Ref_x == 'Ref_01':
                    Ref_01 = Ref_y

            if Ref_1 + Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6 == 0:
                continue

        # Excel okuma ile Analiz satırlarını birleştiriyoruz. 2. Bölüm Değişkenler ile analiz ve rapor souşturma

            elif Check == "Analiz_1":  # Uyumsuz
                Ref_Mix = (Ref_1 * Ref_2)
                if Ref_Mix == 0:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "İncele"

            elif Check == "Analiz_2":  # Uyumsuz
                Ref_Min = (Ref_1 + Ref_2 + Ref_3 + Ref_4)
                Ref_Max = (Ref_1 * Ref_2 * Ref_3 * Ref_4 * Ref_6)
                if Ref_Min == 0:
                    continue
                if not 0 < Ref_Max < 2:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_3":
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                if Ref_1 != Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_4":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5)
                Ref_Max = ((Ref_2 * 4) + (Ref_3 * 4) + (Ref_4 * 4) + (Ref_5 * 4))
                if not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_5":  # Uyumsuz
                Ref_Min = (Ref_1 * 2)
                Ref_Max = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                if not Ref_Min == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_6":  # Uyumsuz
                Ref_Mix = (Ref_1 + Ref_2)
                Ref_Max = ((Ref_3 * 2) + (Ref_4 + Ref_5) + Ref_6)
                if not Ref_Mix == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_7":  # Uyumsuz
                Ref_Mix = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5)
                Ref_Max = ((Ref_2 * 6) + (Ref_3 * 6) + (Ref_4 * 6) + (Ref_5 * 6))
                if Ref_Mix == 0:
                    continue
                if not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_8":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                if Ref_1 == 0:
                    continue
                elif not Ref_1 <= Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_9":  # Uyumsuz
                Ref_Mix = (Ref_1 + Ref_2)
                Ref_Min = (Ref_3 + Ref_4 + Ref_5)
                Ref_Max = ((Ref_3 * 4) + (Ref_4 * 4) + (Ref_5 * 4))
                if Ref_Mix == 0:
                    continue
                if not Ref_Min <= Ref_Mix <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_10":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3)
                Ref_Mix = (Ref_1 * 3)
                Ref_Max = (Ref_1 * 2)

                if Ref_2 != 0 and Ref_3 != 0:
                    if not Ref_1 <= Ref_Min <= Ref_Mix:
                        Sonuc = "Uyumsuz"
                    else:
                        Sonuc = 'Uyumlu'

                elif Ref_2 == 0 and Ref_3 != 0:
                    if not Ref_1 == Ref_3:
                        Sonuc = "Uyumsuz"
                    else:
                        Sonuc = 'Uyumlu'

                elif Ref_2 != 0 and Ref_3 == 0:
                    if not Ref_1 <= Ref_2 <= Ref_Max:
                        Sonuc = "Uyumsuz"
                    else:
                        Sonuc = 'Uyumlu'
                elif Ref_Min == 0:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_11":  # Uyumsuz
                Ref_Max = (((Ref_2 * 2) + (Ref_3 * 4) + (Ref_4 * 2) + Ref_5) - Ref_6)
                if Ref_2 == 0:
                    continue
                elif not Ref_1 == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_12":  # Uyumsuz
                Ref_Max = ((Ref_2 * 2) + (Ref_3 * 2) + (Ref_4 * 2) + (Ref_5 * 2))
                if not Ref_1 == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check in "Analiz_13":  # Uyumsuz
                Ref_Max = (Ref_1 * 2)
                if not Ref_1 <= Ref_2 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_14":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5)
                Ref_Max = (Ref_1 * 6)
                if not Ref_1 <= Ref_Min <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_15":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5)
                Ref_Max = ((Ref_2 * 2) + (Ref_3 * 5) + (Ref_4 * 18))
                if not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_16":  # Uyumsuz
                Ref_Min = (Ref_2 + Ref_3)
                Ref_Max = ((Ref_2 * 2) + (Ref_3 * 4))
                if not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_17":  # Akü - Kablo kontrolü 1-(1+4 or 1-2) + 6201
                Ref_Mix = (Ref_1 * Ref_2)
                Ref_Min = ((Ref_2 - 3) + (Ref_3 * 6))
                Ref_Max = ((Ref_2 + 3) + (Ref_3 * 8))

                if Ref_Mix == 0:
                    Sonuc = "Uyumsuz"
                elif not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_18":  #
                Sonuc = "Bilgi"

            elif Check in "Analiz_19":  #
                if not Ref_1 == Ref_2 and Ref_3 != 0:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_20":  #
                Ref_Mix = (Ref_1 * Ref_2)
                if not Ref_01 == 0:
                    if Ref_Mix == 0:
                        Sonuc = "Uyumsuz"
                    else:
                        Sonuc = "İncele"
                else:
                    continue

            elif Check == "Analiz_21":  #
                Ref_Min = (Ref_3 + Ref_4 + Ref_5 + Ref_6)
                if Ref_1 != Ref_2 or Ref_Min != Ref_1:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_22":
                Ref_Min = (Ref_4 + Ref_5 + Ref_6)
                Ref_Max = ((Ref_4 * 2) + (Ref_5 * 4) + (Ref_6 * 6))
                if not Ref_1 == Ref_2 and Ref_3 == Ref_Min:
                    Sonuc = "Uyumsuz"
                elif not Ref_Min <= Ref_2 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_23":  #
                Ref_Min = (Ref_2 + (Ref_3 / 2))
                if not Ref_1 == Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_24":  #
                Ref_Min = ((Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6) * 4)
                if not Ref_1 == Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_25":
                if Ref_1 != Ref_2:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_26":
                Ref_Min = Ref_1 * Ref_2 * Ref_3
                if Ref_01 > 0:
                    if Ref_Min == 0:
                        Sonuc = "Uyumsuz"
                    else:
                        Sonuc = "Uyumlu"
                else:
                    continue

            # elif Check in Analiz_27:
            #     Ref_Min = (Ref_1 * 2)
            #     if not Ref_1 == Ref_2 == Ref_3 == Ref_4 and Ref_Min == Ref_5:
            #         Sonuc = "Uyumsuz"
            #     else:
            #         Sonuc = "Uyumlu"

            elif Check == "Analiz_28":
                Ref_Min = (Ref_1 + Ref_2)
                Ref_Max = ((Ref_3 * 2) + (Ref_4 * 4) + (Ref_5 * 20))
                if Ref_Min == 0:
                    continue
                elif not Ref_Min <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_29":
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                Ref_Max = (Ref_2 * 1) + ((Ref_3 * 2) + (Ref_4 * 10) + (Ref_5 * 6) + (Ref_6 * 5))
                if not Ref_Min <= Ref_1 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_30":
                Ref_Min = (Ref_1 + Ref_2 + Ref_3)
                Ref_Max = (Ref_4 + Ref_5 + Ref_6)
                if not Ref_Min == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_31":  #
                Ref_Min = (Ref_1 * 4)
                Ref_Max = (Ref_3 * 2)
                if not Ref_1 == Ref_2 == Ref_5 or Ref_1 <= Ref_3 <= Ref_Min or Ref_4 == Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_32":
                if Ref_1 != Ref_2 or Ref_3 != Ref_4:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_33":
                Ref_Min = (Ref_1 * 2)
                if Ref_1 == 0:
                    continue
                elif not Ref_1 == Ref_2 and Ref_Min <= Ref_3:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_34":
                if Ref_01 == 0:
                    continue
                else:
                    Sonuc = "İncele"

            elif Check == "Analiz_35":
                for g in range(0, 10000, 4):
                    if g == Ref_1:
                        Sonuc = "Uyumlu"
                        break
                    elif g > Ref_1:
                        Sonuc = "Uyumsuz"

            elif Check == "Analiz_36":
                if Ref_1 * Ref_2 == 0:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "İncele"

            elif Check == "Analiz_37":
                for g in range(0, 10000, 8):
                    if g == Ref_1:
                        Sonuc = "Uyumlu"
                        break
                    elif g > Ref_1:
                        Sonuc = "Uyumsuz"

            elif Check == "Analiz_38":
                for g in range(0, 10000, 12):
                    if g == Ref_1:
                        Sonuc = "Uyumlu"
                        break
                    elif g > Ref_1:
                        Sonuc = "Uyumsuz"

            elif Check == "Analiz_39":
                Ref_Min = (Ref_3 + Ref_4)
                if not Ref_1 != 0:
                    continue
                elif not Ref_1 <= Ref_2 and Ref_1 <= Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_40":
                Ref_Min = ((Ref_1 + Ref_2 + Ref_3 + Ref_4) * Ref_5)
                Ref_Max = ((Ref_1 + Ref_2 + Ref_3 + Ref_4) * Ref_6)
                Ref_Mix = (Ref_5 * Ref_6)
                if Ref_Min == 0 or Ref_Max == 0 or Ref_Mix == 0:
                    Sonuc = "Uyumlu"
                else:
                    Sonuc = "Uyumsuz"

            elif Check == "Analiz_41":
                if Ref_2 != 0:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_42":
                Ref_Min = (Ref_2 + Ref_3 + Ref_4 + Ref_5 + Ref_6)
                Ref_Max = (Ref_1 * 2)
                if not Ref_1 <= Ref_Min <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_43":
                Ref_Min = (Ref_2 + Ref_3 + Ref_4)
                if not Ref_Min == Ref_1:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            elif Check == "Analiz_44":
                Ref_Min = (Ref_2 + Ref_3)
                if Ref_1 == 0:
                    continue
                if not Ref_1 <= Ref_Min:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"

            # elif Check in Analiz_45:
            #     Ref_Min = (Ref_1 + Ref_2 + Ref_3)
            #     if Ref_Min == 0:
            #         Sonuc = "Uyumsuz"
            #     elif Ref_1 <= Ref_6 or Ref_1 <= Ref_5:
            #         Sonuc = "Uyumsuz"
            #     else:
            #         Sonuc = "Bilgi"

            elif Check == "Analiz_46":
                Ref_Min = (Ref_1 + Ref_2)
                Ref_Max = (Ref_1 + (Ref_2 * 2))
                if not Ref_Min <= Ref_3 <= Ref_Max:
                    Sonuc = "Uyumsuz"
                else:
                    Sonuc = "Uyumlu"
            
                
            if rapor.saha_kod != Saha_Kodu:
                rapor.saha_kod = Saha_Kodu
                rapor.save()
                
            girdi = SayimRapor(saha_no=Saha_Nox, saha_kod=Saha_Kodu, ref_1=Ref_1, ref_2=Ref_2, ref_3=Ref_3, ref_4=Ref_4, ref_5=Ref_5, ref_6=Ref_6, ref_grup=Ref_Grup, sonuc=Sonuc, kontrol=Kontrol, kategori=Kategori, sorgu_no=Sorgu_Nox, rapor=rapor)
            if is_sayim_sonrasi_envanter:
                girdi.is_sayim_sonrasi = True
            girdi.save()
            girdiler.append(girdi)


# Parça Kodlarını Rapora eklenecek <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<

            # parca_kod_list = grupby_data.groupby(by=['Ekipman Parca Kodu', 'Parca Tanimi', 'Ref']).sum()['Quantity'].reset_index()
            # Ref_1 = 0
            # Ref_2 = 0
            # Ref_3 = 0
            # Ref_4 = 0
            # Ref_5 = 0
            # Ref_6 = 0
            # # Birleştirilen tabloda ki genel toplamaların Referans ve toplamların değerleri ayrıştırılır.
            # for f in parca_kod_list.index[0:]:
            #     Ref_Grup = (parca_kod_list.iloc[f, 0])
            #     Kontrol = (parca_kod_list.iloc[f, 1])
            #     Ref_x = (parca_kod_list.iloc[f, 2])
            #     Ref_y = (parca_kod_list.iloc[f, 3])
            #     # Çıktıda ki Referans bilgileri hangi referanslara yazılacağı tespit edilir.
            #     if Ref_x == 'Ref_1':
            #         Ref_1 = Ref_y
            #     elif Ref_x == 'Ref_2':
            #         Ref_2 = Ref_y
            #     elif Ref_x == 'Ref_3':
            #         Ref_3 = Ref_y
            #     elif Ref_x == 'Ref_4':
            #         Ref_4 = Ref_y
            #     elif Ref_x == 'Ref_5':
            #         Ref_5 = Ref_y
            #     elif Ref_x == 'Ref_6':
            #         Ref_6 = Ref_y
            #     df2 = pd.DataFrame({"Saha_No": [Saha_No], "Saha_Kodu": [Saha_Kodu], "1-": [Ref_1], "2-": [Ref_2], "3-": [Ref_3], "4-": [Ref_4], "5-": [Ref_5], "6-": [Ref_6], "Ref_Grup": [Ref_Grup], "Sonuc": [Sonuc], "Kontrol": [Kontrol], "Kategori": [Kategori], "Sorgu_No": [Sorgu_No], "Bilgi": [Ref_x]})
            #     df = df.append(df2)
            #     Ref_1 = 0
            #     Ref_2 = 0
            #     Ref_3 = 0
            #     Ref_4 = 0
            #     Ref_5 = 0
            #     Ref_6 = 0
# Parça Kodlarını Rapora eklenecek <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<

    return girdiler

