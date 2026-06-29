# superAr

O projeto SuperAr possui dois submódulos sendo eles: [superAr_frontEnd](https://github.com/IFRN-auto-cm/superAr-backEnd) e o [superAr_backEnd](https://github.com/IFRN-auto-cm/superAr-frontEnd).

Portanto, para clonar o projeto trazendo os submódulos é necessário executar o comando:
```
git clone --recurse-submodules
```

Por causa dos submódulos existem 3 repositórios: superar, [superAr_frontEnd](https://github.com/IFRN-auto-cm/superAr-backEnd) e [superAr_backEnd](https://github.com/IFRN-auto-cm/superAr-frontEnd). O desenvolvimento está restrito aos repositórios [superAr_frontEnd](https://github.com/IFRN-auto-cm/superAr-backEnd) e [superAr_backEnd](https://github.com/IFRN-auto-cm/superAr-frontEnd) e, portanto, os commits e pushes deverão ser realizados dentro da pasta/repositorio dos submódulos

Como boa prática de projeto os desenvolvedores deverão fazer commits, push e merges para o branch master somente ao ter versões funcionais dos códigos. Enquanto o código estiver em desenvolvimento ou testes, os desenvolvedores deverão utilizar o branch desenvolvimento ou outros branchs. Por tanto após baixar o repo é interessante mudar para o branch de desenvolvimento para começar o trabalho.

Para trocar de um branch para o branch de desenvolvimento se utiliza o comando:

```
git checkout desenvolvimento
```
