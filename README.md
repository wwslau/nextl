# Next L

To use a different bus stop, we can visit below URL to find out your desired bus stop ID.

http://www.nextmuni.com/#!/sf-muni/L/L____I_F00/3601/3599

It seems to me that it only uses the last 4 digits of the stop ID.  

For example, my stop ID is 13601 but 3601 is valid to be used in api call.

Learning here was to traverse the xml tree:

<?xml version="1.0" encoding="utf-8" ?> 
<body copyright="All data copyright San Francisco Muni 2018.">
<predictions agencyTitle="San Francisco Muni" routeTitle="L-Taraval" routeTag="L" stopTitle="Taraval St &amp; 40th Ave" stopTag="6633">
  <direction title="Inbound to West Portal Station">
  <prediction epochTime="1546061699927" seconds="3097" minutes="51" isDeparture="false" affectedByLayover="true" dirTag="L____I_E00" vehicle="1408" block="9509" tripTag="8365951" />
  </direction>
  <direction title="Inbound to Embarcadero Station">
  <prediction epochTime="1546059336817" seconds="734" minutes="12" isDeparture="false" affectedByLayover="true" dirTag="L____I_F00" vehicle="1439" vehiclesInConsist="2" block="9502" tripTag="8365959" />
  <prediction epochTime="1546060356817" seconds="1754" minutes="29" isDeparture="false" affectedByLayover="true" dirTag="L____I_F00" vehicle="1484" vehiclesInConsist="2" block="9507" tripTag="8365958" />
  <prediction epochTime="1546061436817" seconds="2834" minutes="47" isDeparture="false" affectedByLayover="true" dirTag="L____I_F00" vehicle="1527" vehiclesInConsist="2" block="9521" tripTag="8365957" />
  <prediction epochTime="1546062636817" seconds="4034" minutes="67" isDeparture="false" affectedByLayover="true" dirTag="L____I_F00" vehicle="1467" vehiclesInConsist="2" block="9522" tripTag="8365956" />
  <prediction epochTime="1546063836817" seconds="5234" minutes="87" isDeparture="false" affectedByLayover="true" dirTag="L____I_F00" vehicle="1473" vehiclesInConsist="2" block="9501" tripTag="8365955" />
  </direction>
<message text="Starting 8pm Dec. 31 until 5am Jan. 1 Ride Muni Free for New Years Eve" priority="Low"/>
</predictions>
</body>

