#!/usr/bin/env python3
import urdhva_tiryagbhyam, nikhilam, anurupyena, yavadunam, sankalana, paravartya, shunyam

print("Urdhva: 123*456 =", urdhva_tiryagbhyam.urdhva_multiply(123,456))
print("Nikhilam: 98*97 =", nikhilam.nikhilam_multiply(98,97))
print("Anurupyena: 1234*1005 =", anurupyena.anurupyena_multiply(1234,1005))
print("Yavadunam: 96^2 =", yavadunam.yavadunam_square(96))
print("Sankalana: sum=100,diff=20 ->", sankalana.sankalana_solve(100,20))
print("Paravartya: 2x+3y=8, 5x-y=3 ->", paravartya.paravartya_solve(2,3,8,5,-1,3))
print("Shunyam: compressing 'Vedic Vedic Pattern' ->", shunyam.shunyam_compress("Vedic Vedic Pattern")[0])
