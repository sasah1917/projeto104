import cv2

img = cv2.imread('solar-system.jpg') 

cv2.imshow('resultado',img)

cv2.waitKey(0)

cv2.putText(img,
            "sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )


cv2.putText(img,
            "Mercurio",
            (100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (60, 43, 62)
            )



cv2.putText(img,
            "venus",
            (100,170),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (196, 130, 55)
            )


cv2.putText(img,
            "terra",
            (100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (47, 119, 133)
            )


cv2.putText(img,
            "marte",
            (100,230),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (204, 149, 87)
            )


cv2.putText(img,
            "jupter",
            (100,250),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (132, 128, 130)
            )


cv2.putText(img,
            "saturno",
            (100,280),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (153, 128, 93)
            )


cv2.putText(img,
            "urano",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (209, 243, 245)
            )


cv2.putText(img,
            "netuno",
            (100,350),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (70, 110, 250)
            )

cv2.imwrite('Solar_systemwithname.jpg',img)