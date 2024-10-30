# Keyingi Palindrom Sonni Topish
# Kod doppi dasturlash tilida yozilgan
Ushbu kod berilgan sondan boshlanib, **keyingi palindrom son** topish jarayonini amalga oshiradi. Kodda **palindrom** — sonni teskari yozilganda ham o'ziga teng bo'lgan son sifatida aniqlanadi.

## Funksiya Tafsiloti

### `isPalindrome(num)` funksiyasi:
- **Parametr**: `num` — tekshirilishi kerak bo'lgan son.
- **Vazifasi**: Son teskari o'qilganda ham bir xil bo'lsa, 1 qaytaradi, aks holda 0 qaytaradi.

#### Funksiya ishlash jarayoni:
1. O'zgaruvchilar (`n`, `k`, `rev`) e'lon qilinadi va `rev` 0 ga tenglanadi.
2. `num` ning qiymati `n` ga saqlanadi, shunda uni keyin teskari ko'rinishi bilan solishtiramiz.
3. **Tsikl** (`toki`) orqali:
   - Har bir raqamni ajratib olamiz va `rev` ga qo'shamiz.
   - `num` qiymatini qisqartiramiz (`yaxlitla` yordamida).
4. Agar **berilgan son** va uning **teskari ko'rinishi** bir xil bo'lsa, 1 qaytaradi, aks holda 0.

---

## Boshqaruvchi Kod

1. **Boshlang'ich son**: `num := 9687`.
2. Agar son palindrom bo'lmasa, tsikl orqali (`toki`) **keyingi son**ga o'tib boramiz.
3. **Natija**: Palindrom son topilgach, ekranga chiqariladi.

---

## Ishlash Namoyishi

```doppi
yarat num := 9687;

toki(isPalindrome(num) == 0) {
    num := num + 1;
};

chiqar("Next Palindrome :", num);```
