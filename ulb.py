import mysql.connector as mc

try:

    # ---- connexion a la bdd
    conn = mc.connect(host = 'localhost', database = "ulb", user ="root", password="")
    cursor = conn.cursor()
    # ----

    rang_etudiant_desc = []
  
    ordre_etudiant_specifique_annexe_1 = []
    hopital_etudiant_specifique_annexe_1 = []
    service_etudiant_specifique_annexe_1 = []
    typePref_etudiant_specifique_annexe_1 = []



    hopital_places_annexe_5 = []
    service_places_annexe_5 = []
    places_places_annexe_5 = []


    etudiant_stage_trouve = []
    etudiant_stage_non_trouve = []

    id_etudiant_preference_2 = []
    id_hopital_preference_2 = []
    id_service_preference_2 = []

    

    # ---- trier les etudiants en fonction du rang du plus grand au plus petit de l'annexe 2
    def tri_rang_etudiant():
        rang_etudiant_sql = "select matricule, rang from ordrechoixstages order by rang desc"
        cursor.execute(rang_etudiant_sql)
        list = cursor.fetchall()

        for list2 in list:

            # matricule:
            rang_etudiant_desc.append(list2[0])
        
    tri_rang_etudiant()
    # ----


    # ---- Trier en fonction de l'odre des etudiants en specifiants le matricule
    def ordre_etudiant_specifique(matricule_etudiant):
        rang_etudiant_sql = "select matricule, ordre, hopital, service, typePref from prefschoixstages where matricule = {} order by ordre desc;".format(matricule_etudiant)
        cursor.execute(rang_etudiant_sql)

        list = cursor.fetchall()


        for list2 in list:
            # ordre:
            ordre_etudiant_specifique_annexe_1.append(list2[1])

            # hopital
            hopital_etudiant_specifique_annexe_1.append(list2[2])

            # service
            service_etudiant_specifique_annexe_1.append(list2[3])

            # typePref
            typePref_etudiant_specifique_annexe_1.append(list2[4])

            
    # ----


    # ---- trier les hopitaux et les services de l'annexe 1 en focntion du matricule
    def tri_hopitaux_services(matricule_etudiant):
        rang_etudiant_sql = "select matricule, hopital, service from prefschoixstages where matricule = {} order by ordre desc;".format(matricule_etudiant)
        cursor.execute(rang_etudiant_sql)
        
        list = cursor.fetchall()

        for list2 in list:
            print("Hopital : {},".format(list2[1]), "service : {},".format(list2[2]))
           
    # ----
    
    
    
    # ---- Trier les places, services et hopitaux de l'annexe 5
    def places_annexe_5(hopital, service):
        rang_etudiant_sql = "select id, hopital, service, places from places where hopital = {} and service = {};".format(hopital, service)
        cursor.execute(rang_etudiant_sql)
        
        list = cursor.fetchall()

        for list2 in list:
            print("Hopital : {},".format(list2[1]), "service : {},".format(list2[2]), "places : {}".format(list2[3]))

            # --- hopital
            hopital_places_annexe_5.append(list2[1])

            # --- service
            service_places_annexe_5.append(list2[2])

            # --- places
            places_places_annexe_5.append(list2[3])
    # ----


    
    # ---- Mets les étudiants qui n'ont pas trouvé de stage dans une liste.
    for i in rang_etudiant_desc:
        etudiant_stage_non_trouve.append(i)
    # ----

    
    
    


    # ---- creation de la fonction principale
    def main_prog():

        for e in range(0, len(rang_etudiant_desc), 1): # lister chaque etudiants
            id_etudiant = rang_etudiant_desc[e]
            ordre_etudiant_specifique(id_etudiant) # affiche l'ordre de l'etudiant en fonction du matricule de rang_etudiant_desc


            for x in range(0, len(hopital_etudiant_specifique_annexe_1), 1): # lister chaque hopital et son service
                id_hopital = hopital_etudiant_specifique_annexe_1[x] # faire +1 en focntion de la taille de liste de hopital et apres faire +1 au id_etudiant
                id_service = service_etudiant_specifique_annexe_1[x]
                places_annexe_5(id_hopital, id_service)
                


                if places_places_annexe_5[0] >= 1: # Verifie si il y'a encore de la place
                    place_sql = "UPDATE `places` SET `places` = '0' WHERE hopital = {} and service = {}".format(hopital_etudiant_specifique_annexe_1[x], service_etudiant_specifique_annexe_1[x])
                    cursor.execute(place_sql)
                    print("l'etudiant {}".format(id_etudiant), "à trouvé une place dans l'hopital {}".format(id_hopital), "dans le service {}".format(id_service))
                    etudiant_stage_trouve.append(id_etudiant)


                    if typePref_etudiant_specifique_annexe_1[0] == "1": # on verifie la preference de l'etudiant (1 ou 2)
                        print("preference ", typePref_etudiant_specifique_annexe_1[0])
                        

                    elif typePref_etudiant_specifique_annexe_1[0] == "2":
                        id_etudiant_preference_2.append("{} ".format(id_etudiant))
                        id_hopital_preference_2.append("{}".format(id_hopital))
                        id_service_preference_2.append("{}".format(id_service))
                    


                else:
                    # VERIFIER LA PLACE
                    print("il n'y a plus de place, annexe suivante")
                
    # ----
                    
                    
                    



                       
                    

    # ---- verifier si les etudiants on deja un stage

    if not etudiant_stage_trouve:
        main_prog()
    

    else:
        for x in etudiant_stage_trouve:
            if id_etudiant == x:
                print("L'etudiant {}".format(id_etudiant), "a deja trouvé aun stage")

    # ----
        




    


    









except mc.Error as err:
    print(err)


finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()

























