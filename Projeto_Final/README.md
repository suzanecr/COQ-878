Abaixo estão os nomes de cada código utilizado para realização deste projeto e a que cada código se destina.

I) Criação da caixa de simulação.

* Otimização da estrutura .cif da hidroxiapatita: OTIM_MACE.ipynb → colab com GPU
* Criação da caixa com o etanol (etanol criado pelo próprio ASE): EtOH_HAP.ipynb → WSL

II) Dinâmica molecular com MACE

* Etapa de equilibração: EQUIL_MACE.ipynb → colab com GPU
* Etapa de produção: PROD_MACE.ipynb → colab com GPU
* Fine-Tunning: FT_MACE.ipynb → colab com GPU

III) Escolha do frame para etapa de produção.

* Escolha do frame: Frame.ipynb → colab sem GPU

IV) Cálculo ab initio com o VASP

* Após produção: MACE_VASP_production.py → Cluster
* Após Fine-Tunning: Fine_Tunning.py → Cluster
 
V) Comparação dos resultados:

* Plot para comparação: plot_MACE.ipynb → colab sem GPU
