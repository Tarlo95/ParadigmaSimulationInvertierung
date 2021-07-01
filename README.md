# ParadigmaSimulationInvertierung
Test um Invertierung während des Versuchs möglich zu machen

Der Code ist im Branch master (sorry, verschieben hab ich nicht gebacken bekommen)

Beim starten des Codes sollte sich ein kleines Spiel öffnen.
falls es pygame nicht finden kann folgendes in den Terminal eingeben um die Bibliothek herunterzuladen: python3 -m pip install -U pygame --user

/br Was sieht man?
Der Kreis auf der oberen Linie soll die Hand bzw den Controller darstellen.
Der Kreis auf der unteren Linie soll die virtuelle Hand darstellen

Beim klicken mit der Maus wird die virtuelle Hand invertiert.
Um ein Springen zu verhindern, werden die Referenzpunkte der Hand und der virtuellen Hand neu an den aktuelen Positionen gesetzt.
Um trotzdem an jede Position zu kommen, werden die beiden Referenzpunkte (bzw deren dazugehörigen "Strecken" auf der Linie) ins Verhältnis gesetzt. Ist also die Hand auf halber Strecke zwischen beginn der Linie und Referenzpunkt, ist dies auch bei der virtuellen Hand der Fall. 
Um das Problem des plötzlichen sensibilitätsunterschieds beim "überfahren" des Punktes zu beheben (wenn dieser nicht gewünscht ist), könnten die berechneten Konstanten (Faktor1 und Faktor2 im Code) in einer Funktion in Abhängigkeit der Entfernung vom Referenzpunkt verwendet werden. Somit könnte man zum Beispiel eine niedrige Sensibilität um den Referenzpunkt und eine hohe Sensibilität, je weiter man sich von diesem Entfernt erreichen.

Um zu große Faktoren (und damit sehr hohe Sensibilitäten) zu vermeiden, gibt es einen Sicherheitsabstand zum Rand, in dem kein Klicken möglich ist. Im echten Programm mit 3 Achsen könnte man stattdessen auf die beiden anderen Achsen zugreifen und bei denen eine Invertierung bzw Manipulation vornehmen.
