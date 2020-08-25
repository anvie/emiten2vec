Emiten2Vec
-------------

Emiten2Vec adalah _pretrained model_ Word2Vec yang ditrain pada dataset berita saham Indonesia sejak tahun 2015 sampai Juli 2020.

## Pasang

Emiten2Vec membutuhkan dependensi librari Python `gensim`, pasang dengan:

```
$ pip install gensim
```

## Ujicoba

Contoh penggunaan:

```
$ python emiten2vec.py --model=model/emiten2vec.model
Memuat...
> Masukkan kata kunci: bbri
   * bmri       0.9300627112388611
   * bbni       0.9034568071365356
   * bbca       0.8930842876434326
   * tlkm       0.8450931906700134
   * bbtn       0.7917706370353699
   * cpin       0.758827269077301
   * hmsp       0.7337543368339539
   * unvr       0.7268385291099548
   * asii       0.7200209498405457
   * bmr        0.718830406665802
```

```
> Masukkan kata kunci: indosat
   * ooredoo    0.9149157404899597
   * isat       0.8860697746276855
   * xl 0.8580667972564697
   * axiata     0.8442668914794922
   * excl       0.7415362596511841
   * smartfren  0.731278121471405
   * seluler    0.7136989235877991
   * ooredo     0.7080795764923096
   * telkomsel  0.7066589593887329
   * telkom     0.6999109983444214
```

```
> Masukkan kata kunci: hmsp
   * ggrm       0.9463620185852051
   * hm 0.8448810577392578
   * cpin       0.8196327686309814
   * unvr       0.8106383681297302
   * garam      0.7835429310798645
   * hanjaya    0.7816216349601746
   * tlkm       0.7780724167823792
   * asii       0.7633928656578064
   * bbca       0.7592865228652954
   * wiim       0.7496331930160522
```

Semoga bermanfaat!

[] Robin Sy
