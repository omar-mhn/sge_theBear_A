# sge_theBear_A

## Diagrama entitat - relació 

![SGE_A_final.drawio.png](Capturas/MdoelE-R/SGE_A_final.drawio.png)

# Captures del Swagger funcionant

## Farem un exemple amb una de les taules del model, en aquest cas amb "Client". Començarem creant un registre amb l'endpoint POST:

![Client_Post.png](Capturas/Swagger/Client_Post.png)

Després comprovarem que s'hagi creat satisfactòriament amb els dos mètodes GET que tenim, el primer que mira tots els registres de la taula.

![Client_GetAll.png](Capturas/Swagger/Client_GetAll.png)

i el següent que mira segons l'id:

![Client_GetId.png](Capturas/Swagger/Client_GetId.png)

Ara actualitzarem el registre creat prèviament. Tenim dos mètodes PUT, un que actualitza tots els camps i altre que només actualitza el camp que l'indiques. 
Aquí veiem el que actualitza tots els camps:

![Client_Update.png](Capturas/Swagger/Client_Update.png)

Aquí l'altre:

![Client_UpdateField.png](Capturas/Swagger/Client_UpdateField.png)

Comprovem com queda el registre després de les actualitzacions:

![Client_abansDeDelete.png](Capturas/Swagger/Client_abansDeDelete.png)

Ara esborrarem el registre amb el mètode DELETE:

![Client_Del.png](Capturas/Swagger/Client_Del.png)

I comprovem que s'hagi esborrat:

![ClientDespresDel.png](Capturas/Swagger/ClientDespresDel.png)

Ara es mostraran la resta de taules en el mateix ordre de captures: crear, mostrar tot, mostrar per id, actualitzar tot i actualitzar el camp seleccionat, mostrar les dades actualitzades, esborrar i mostrar que s'ha esborrat satisfactòriament el registre.

## Taula Planificació

![Planificacio_Post.png](Capturas/Swagger/Planificacio_Post.png)

![Plani_GetAll.png](Capturas/Swagger/Plani_GetAll.png)

![PLani_GetId.png](Capturas/Swagger/PLani_GetId.png)

![Plani_Update.png](Capturas/Swagger/Plani_Update.png)

![Plani_UpdateField.png](Capturas/Swagger/Plani_UpdateField.png)

![Plani_abansDelete.png](Capturas/Swagger/Plani_abansDelete.png)

![Plani_Del.png](Capturas/Swagger/Plani_Del.png)

![Plani_despresDel.png](Capturas/Swagger/Plani_despresDel.png)

## Taula Proveïdor

![Preveidor_Post.png](Capturas/Swagger/Preveidor_Post.png)

![Proveidor_GetAll.png](Capturas/Swagger/Proveidor_GetAll.png)

![Proveidor_GetId.png](Capturas/Swagger/Proveidor_GetId.png)

![Proveidors_Update.png](Capturas/Swagger/Proveidors_Update.png)

![Proveidor_UpdateField.png](Capturas/Swagger/Proveidor_UpdateField.png)

![Proveidor_abans Delete.png](Capturas/Swagger/Proveidor_abans%20Delete.png)

![Proveidor_Del.png](Capturas/Swagger/Proveidor_Del.png)

![ProveidorDespresDel.png](Capturas/Swagger/ProveidorDespresDel.png)

## Taula Reunió

![Reunio_Post.png](Capturas/Swagger/Reunio_Post.png)

![Reunio_GetAll.png](Capturas/Swagger/Reunio_GetAll.png)

![Reunio_GetId.png](Capturas/Swagger/Reunio_GetId.png)

![Reunio_Update.png](Capturas/Swagger/Reunio_Update.png)

![Reunio_UpdateField.png](Capturas/Swagger/Reunio_UpdateField.png)

![Reunio_abansDelete.png](Capturas/Swagger/Reunio_abansDelete.png)

![Reunio_Del.png](Capturas/Swagger/Reunio_Del.png)

![Reunio_despresDel.png](Capturas/Swagger/Reunio_despresDel.png)

## Taula Vendre

![Vendre_Post.png](Capturas/Swagger/Vendre_Post.png)

![Vendre_GetAll.png](Capturas/Swagger/Vendre_GetAll.png)

![Vendre_GetId.png](Capturas/Swagger/Vendre_GetId.png)

![Vendre_Update.png](Capturas/Swagger/Vendre_Update.png)

![Vendre_UpdateField.png](Capturas/Swagger/Vendre_UpdateField.png)

![Vendre_abansDelete.png](Capturas/Swagger/Vendre_abansDelete.png)

![Vendre_Del.png](Capturas/Swagger/Vendre_Del.png)

![Vendre_despresDel.png](Capturas/Swagger/Vendre_despresDel.png)

## Taula Empleat

![Empleat_Post.png](Capturas/Swagger/Empleat_Post.png)

![Empleat_GetAll.png](Capturas/Swagger/Empleat_GetAll.png)

![Empleat_GetId.png](Capturas/Swagger/Empleat_GetId.png)

![Empleat_Update.png](Capturas/Swagger/Empleat_Update.png)

![Empleat_UpdateField.png](Capturas/Swagger/Empleat_UpdateField.png)

![Empleat_Del.png](Capturas/Swagger/Empleat_Del.png)

## Taula Inventari

![Inventari_Post.png](Capturas/Swagger/Inventari_Post.png)

![Inventari_GetAll.png](Capturas/Swagger/Inventari_GetAll.png)

![Inventari_GetId.png](Capturas/Swagger/Inventari_GetId.png)

![Inventari_Update.png](Capturas/Swagger/Inventari_Update.png)

![Inventari_UpdateField.png](Capturas/Swagger/Inventari_UpdateField.png)

![Inventari_Del.png](Capturas/Swagger/Inventari_Del.png)

## Taula Reserva
![reserva_Post.png](Capturas/Swagger/reserva_Post.png)

![reserva_GetAll.png](Capturas/Swagger/reserva_GetAll.png)

![reserva_GetId.png](Capturas/Swagger/reserva_GetId.png)

![reserva_Update.png](Capturas/Swagger/reserva_Update.png)

![reserva_UpdateField.png](Capturas/Swagger/reserva_UpdateField.png)

![reserva_abansDelete.png](Capturas/Swagger/reserva_abansDelete.png)

![reserva_Del.png](Capturas/Swagger/reserva_Del.png)

![reserva_despresDel.png](Capturas/Swagger/reserva_despresDel.png)

## Taula Comanda 
![comanda_Post.png](Capturas/Swagger/comanda_Post.png)

![comanda_GetAll.png](Capturas/Swagger/comanda_GetAll.png)

![comanda_GetId.png](Capturas/Swagger/comanda_GetId.png)

![comanda_Update.png](Capturas/Swagger/comanda_Update.png)

![comanda_UpdateField.png](Capturas/Swagger/comanda_UpdateField.png)

![comanda_abansDelete.png](Capturas/Swagger/comanda_abansDelete.png)

![comanda_Del.png](Capturas/Swagger/comanda_Del.png)

![comanda_despresDel.png](Capturas/Swagger/comanda_despresDel.png)

## Taula Coste 
![coste_post.png](Capturas/Swagger/coste_post.png)

![coste_GetAll.png](Capturas/Swagger/coste_GetAll.png)

![coste_GetId.png](Capturas/Swagger/coste_GetId.png)

![coste_Update.png](Capturas/Swagger/coste_Update.png)

![coste_UpdateField.png](Capturas/Swagger/coste_UpdateField.png)

![coste_abansDelete.png](Capturas/Swagger/coste_abansDelete.png)

![coste_Del.png](Capturas/Swagger/coste_Del.png)

![coste_despresDel.png](Capturas/Swagger/coste_despresDel.png)

## Taula Participar 
![participar_post.png](Capturas/Swagger/participar_post.png)

![participar_GetAll.png](Capturas/Swagger/participar_GetAll.png)

![participar_GetId.png](Capturas/Swagger/participar_GetId.png)

![participar_abansDelete.png](Capturas/Swagger/participar_abansDelete.png)

![participar_Del.png](Capturas/Swagger/participar_Del.png)

![participar_despresDel.png](Capturas/Swagger/participar_despresDel.png)

## Taula Producte 
![producte_Post.png](Capturas/Swagger/producte_Post.png)

![producte_GetAll.png](Capturas/Swagger/producte_GetAll.png)

![producte_GetId.png](Capturas/Swagger/producte_GetId.png)

![producte_Update.png](Capturas/Swagger/producte_Update.png)

![producte_UpdateField.png](Capturas/Swagger/producte_UpdateField.png)

![producte_abansDelete.png](Capturas/Swagger/producte_abansDelete.png)

![producte_Del.png](Capturas/Swagger/producte_Del.png)

![producte_despresDel.png](Capturas/Swagger/producte_despresDel.png)

## Taula Producte_Final
![producte_final_Post.png](Capturas/Swagger/producte_final_Post.png)

![producte_final_GetAll.png](Capturas/Swagger/producte_final_GetAll.png)

![producte_final_GetId.png](Capturas/Swagger/producte_final_GetId.png)

![producte_final_Update.png](Capturas/Swagger/producte_final_Update.png)

![producte_final_UpdateField.png](Capturas/Swagger/producte_final_UpdateField.png)

![producte_final_abansDelete.png](Capturas/Swagger/producte_final_abansDelete.png)

![producte_final_Del.png](Capturas/Swagger/producte_final_Del.png)

![producte_final_despresDel.png](Capturas/Swagger/producte_final_despresDel.png)
