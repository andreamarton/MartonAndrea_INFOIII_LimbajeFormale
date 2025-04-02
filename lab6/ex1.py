def pumping_lemma_L1(nr_pompare):

        print("1. L = {0^i 1^j | i > j}")

        cuvant_ex = '0' * (nr_pompare + 1) + '1' * nr_pompare
        print(f"Stringul generat: {cuvant_ex}")

        for lungime_y in range(1, nr_pompare + 1):
            parte_x = cuvant_ex[:nr_pompare + 1 - lungime_y]
            parte_z = cuvant_ex[nr_pompare + 1:]

            cvt_pompat = parte_x + parte_z
            numar_0 = cvt_pompat.count('0')
            numar_1 = cvt_pompat.count('1')

            if numar_0 <= numar_1:
                print("Limbaj neregulat")
                return


def pumping_lemma_L2(nr_pompare):

    print("2. L = {a^i b^j | i <= j}")

    cuvant_ex = 'a' * nr_pompare + 'b' * (nr_pompare + 1)
    print(f"Stringul generat: {cuvant_ex}")

    for lungime_y in range(1, nr_pompare + 1):
        parte_x = cuvant_ex[:nr_pompare - lungime_y]
        parte_y = cuvant_ex[nr_pompare - lungime_y:nr_pompare]
        parte_z = cuvant_ex[nr_pompare:]

        cvt_pompat1 = parte_x + parte_y + parte_y + parte_z
        numar_a = cvt_pompat1.count('a')
        numar_b = cvt_pompat1.count('b')

        if numar_a > numar_b:
            print("Limbaj neregulat")
            return


def pumping_lemma_L3(nr_pompare):

    print("3. L = {a^n b^n c^n | n > 0}")

    cuvant_ex = 'a' * nr_pompare + 'b' * nr_pompare + 'c' * nr_pompare
    print(f"String generat: {cuvant_ex}")

    for start_y in range(nr_pompare):
        for lungime_y in range(1, nr_pompare + 1):
            if start_y + lungime_y <= len(cuvant_ex):
                parte_x = cuvant_ex[:start_y]
                parte_y = cuvant_ex[start_y:start_y + lungime_y]
                parte_z = cuvant_ex[start_y + lungime_y:]

                cvt_pompat = parte_x + parte_y + parte_y + parte_z
                print(f"Pompare (y='{parte_y}'): {cvt_pompat}")

                numar_a = cvt_pompat.split('b')[0].count('a')
                numar_b = cvt_pompat[numar_a:].split('c')[0].count('b')
                numar_c = len(cvt_pompat) - numar_a - numar_b

                if numar_a != numar_b or numar_b != numar_c: 
                    print("Limbaj neregulat")
                    return


pumping_lemma_L1(2)
pumping_lemma_L2(2)
pumping_lemma_L3(2)
