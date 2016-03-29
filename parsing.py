stuff = """
<tr><td class="tna">1</td><td class="tna"><a name="AL"></a><a href="AL-D">Alabama</a></td><td class="tna">63.0</td><td class="tna">6.0</td><td class="tba">69.0</td><td class="tna">41 district / 14 at large; 8 Pledged PLEOs;<br>6 Unpledged PLEOs</td></tr>
<tr><td class="tnb">2</td><td class="tnb"><a name="AK"></a><a href="AK-D">Alaska</a></td><td class="tnb">19.0</td><td class="tnb">5.0</td><td class="tbb">24.0</td><td class="tnb">12 district / 5 at large; 2 Pledged PLEOs;<br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">3</td><td class="tna"><a name="AS"></a><a href="AS-D">American Samoa</a></td><td class="tna">6.0</td><td class="tna">6.0</td><td class="tba">12.0</td><td class="tna">6 at large; <br>6 Unpledged PLEOs</td></tr>
<tr><td class="tnb">4</td><td class="tnb"><a name="AZ"></a><a href="AZ-D">Arizona</a></td><td class="tnb">70.0</td><td class="tnb">10.0</td><td class="tbb">80.0</td><td class="tnb">46 district / 15 at large; 9 Pledged PLEOs;<br>10 Unpledged PLEOs</td></tr>
<tr><td class="tna">5</td><td class="tna"><a name="AR"></a><a href="AR-D">Arkansas</a></td><td class="tna">47.0</td><td class="tna">8.0</td><td class="tba">55.0</td><td class="tna">31 district / 11 at large; 5 Pledged PLEOs;<br>8 Unpledged PLEOs</td></tr>
<tr><td class="tnb">6</td><td class="tnb"><a name="CA"></a><a href="CA-D">California</a></td><td class="tnb">547.0</td><td class="tnb">62.0</td><td class="tbb">609.0</td><td class="tnb">365 district / 121 at large; 61 Pledged PLEOs;<br>62 Unpledged PLEOs</td></tr>
<tr><td class="tna">7</td><td class="tna"><a name="CO"></a><a href="CO-D">Colorado</a></td><td class="tna">72.0</td><td class="tna">14.0</td><td class="tba">86.0</td><td class="tna">47 district / 16 at large; 9 Pledged PLEOs;<br>14 Unpledged PLEOs</td></tr>
<tr><td class="tnb">8</td><td class="tnb"><a name="CT"></a><a href="CT-D">Connecticut</a></td><td class="tnb">73.0</td><td class="tnb">15.0</td><td class="tbb">88.0</td><td class="tnb">49 district / 16 at large; 8 Pledged PLEOs;<br>15 Unpledged PLEOs</td></tr>
<tr><td class="tna">9</td><td class="tna"><a name="DE"></a><a href="DE-D">Delaware</a></td><td class="tna">23.0</td><td class="tna">10.0</td><td class="tba">33.0</td><td class="tna">15 district / 5 at large; 3 Pledged PLEOs;<br>10 Unpledged PLEOs</td></tr>
<tr><td class="tnb">10</td><td class="tnb"><a name="DA"></a><a href="DA-D">Democrats Abroad</a></td><td class="tnb">15.0</td><td class="tnb">4.0</td><td class="tbb">19.0</td><td class="tnb">14 at large; 1 Pledged PLEO;<br>4 Unpledged PLEOs</td></tr>
<tr><td class="tna">11</td><td class="tna"><a name="DC"></a><a href="DC-D">District of Columbia</a></td><td class="tna">22.0</td><td class="tna">23.0</td><td class="tba">45.0</td><td class="tna">14 district / 5 at large; 3 Pledged PLEOs;<br>23 Unpledged PLEOs</td></tr>
<tr><td class="tnb">12</td><td class="tnb"><a name="FL"></a><a href="FL-D">Florida</a></td><td class="tnb">276.0</td><td class="tnb">24.0</td><td class="tbb">300.0</td><td class="tnb">184 district / 61 at large; 31 Pledged PLEOs;<br>24 Unpledged PLEOs</td></tr>
<tr><td class="tna">13</td><td class="tna"><a name="GA"></a><a href="GA-D">Georgia</a></td><td class="tna">110.0</td><td class="tna">14.0</td><td class="tba">124.0</td><td class="tna">72 district / 24 at large; 14 Pledged PLEOs;<br>14 Unpledged PLEOs</td></tr>
<tr><td class="tnb">14</td><td class="tnb"><a name="GU"></a><a href="GU-D">Guam</a></td><td class="tnb">7.0</td><td class="tnb">5.0</td><td class="tbb">12.0</td><td class="tnb">7 at large; <br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">15</td><td class="tna"><a name="HI"></a><a href="HI-D">Hawaii</a></td><td class="tna">26.0</td><td class="tna">9.0</td><td class="tba">35.0</td><td class="tna">17 district / 6 at large; 3 Pledged PLEOs;<br>9 Unpledged PLEOs</td></tr>
<tr><td class="tnb">16</td><td class="tnb"><a name="ID"></a><a href="ID-D">Idaho</a></td><td class="tnb">27.0</td><td class="tnb">4.0</td><td class="tbb">31.0</td><td class="tnb">18 district / 6 at large; 3 Pledged PLEOs;<br>4 Unpledged PLEOs</td></tr>
<tr><td class="tna">17</td><td class="tna"><a name="IL"></a><a href="IL-D">Illinois</a></td><td class="tna">189.0</td><td class="tna">26.0</td><td class="tba">215.0</td><td class="tna">123 district / 41 at large; 25 Pledged PLEOs;<br>26 Unpledged PLEOs</td></tr>
<tr><td class="tnb">18</td><td class="tnb"><a name="IN"></a><a href="IN-D">Indiana</a></td><td class="tnb">96.0</td><td class="tnb">9.0</td><td class="tbb">105.0</td><td class="tnb">63 district / 22 at large; 11 Pledged PLEOs;<br>9 Unpledged PLEOs</td></tr>
<tr><td class="tna">19</td><td class="tna"><a name="IA"></a><a href="IA-D">Iowa</a></td><td class="tna">54.0</td><td class="tna">11.0</td><td class="tba">65.0</td><td class="tna">35 district / 12 at large; 7 Pledged PLEOs;<br>11 Unpledged PLEOs</td></tr>
<tr><td class="tnb">20</td><td class="tnb"><a name="KS"></a><a href="KS-D">Kansas</a></td><td class="tnb">49.0</td><td class="tnb">4.0</td><td class="tbb">53.0</td><td class="tnb">33 district / 11 at large; 5 Pledged PLEOs;<br>4 Unpledged PLEOs</td></tr>
<tr><td class="tna">21</td><td class="tna"><a name="KY"></a><a href="KY-D">Kentucky</a></td><td class="tna">66.0</td><td class="tna">7.0</td><td class="tba">73.0</td><td class="tna">45 district / 14 at large; 7 Pledged PLEOs;<br>7 Unpledged PLEOs</td></tr>
<tr><td class="tnb">22</td><td class="tnb"><a name="LA"></a><a href="LA-D">Louisiana</a></td><td class="tnb">64.0</td><td class="tnb">8.0</td><td class="tbb">72.0</td><td class="tnb">42 district / 14 at large; 8 Pledged PLEOs;<br>8 Unpledged PLEOs</td></tr>
<tr><td class="tna">23</td><td class="tna"><a name="ME"></a><a href="ME-D">Maine</a></td><td class="tna">31.0</td><td class="tna">6.0</td><td class="tba">37.0</td><td class="tna">20 district / 7 at large; 4 Pledged PLEOs;<br>6 Unpledged PLEOs</td></tr>
<tr><td class="tnb">24</td><td class="tnb"><a name="MD"></a><a href="MD-D">Maryland</a></td><td class="tnb">97.0</td><td class="tnb">27.0</td><td class="tbb">124.0</td><td class="tnb">64 district / 21 at large; 12 Pledged PLEOs;<br>27 Unpledged PLEOs</td></tr>
<tr><td class="tna">25</td><td class="tna"><a name="MA"></a><a href="MA-D">Massachusetts</a></td><td class="tna">110.0</td><td class="tna">26.0</td><td class="tba">136.0</td><td class="tna">72 district / 24 at large; 14 Pledged PLEOs;<br>26 Unpledged PLEOs</td></tr>
<tr><td class="tnb">26</td><td class="tnb"><a name="MI"></a><a href="MI-D">Michigan</a></td><td class="tnb">183.0</td><td class="tnb">20.0</td><td class="tbb">203.0</td><td class="tnb">122 district / 41 at large; 20 Pledged PLEOs;<br>20 Unpledged PLEOs</td></tr>
<tr><td class="tna">27</td><td class="tna"><a name="MN"></a><a href="MN-D">Minnesota</a></td><td class="tna">91.0</td><td class="tna">16.0</td><td class="tba">107.0</td><td class="tna">59 district / 20 at large; 12 Pledged PLEOs;<br>16 Unpledged PLEOs</td></tr>
<tr><td class="tnb">28</td><td class="tnb"><a name="MS"></a><a href="MS-D">Mississippi</a></td><td class="tnb">40.0</td><td class="tnb">5.0</td><td class="tbb">45.0</td><td class="tnb">26 district / 9 at large; 5 Pledged PLEOs;<br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">29</td><td class="tna"><a name="MO"></a><a href="MO-D">Missouri</a></td><td class="tna">89.0</td><td class="tna">13.0</td><td class="tba">102.0</td><td class="tna">58 district / 19 at large; 12 Pledged PLEOs;<br>13 Unpledged PLEOs</td></tr>
<tr><td class="tnb">30</td><td class="tnb"><a name="MT"></a><a href="MT-D">Montana</a></td><td class="tnb">24.0</td><td class="tnb">7.0</td><td class="tbb">31.0</td><td class="tnb">16 district / 6 at large; 2 Pledged PLEOs;<br>7 Unpledged PLEOs</td></tr>
<tr><td class="tna">31</td><td class="tna"><a name="NE"></a><a href="NE-D">Nebraska</a></td><td class="tna">38.0</td><td class="tna">6.0</td><td class="tba">44.0</td><td class="tna">25 district / 9 at large; 4 Pledged PLEOs;<br>6 Unpledged PLEOs</td></tr>
<tr><td class="tnb">32</td><td class="tnb"><a name="NV"></a><a href="NV-D">Nevada</a></td><td class="tnb">36.0</td><td class="tnb">8.0</td><td class="tbb">44.0</td><td class="tnb">23 district / 8 at large; 5 Pledged PLEOs;<br>8 Unpledged PLEOs</td></tr>
<tr><td class="tna">33</td><td class="tna"><a name="NH"></a><a href="NH-D">New Hampshire</a></td><td class="tna">28.0</td><td class="tna">7.0</td><td class="tba">35.0</td><td class="tna">18 district / 6 at large; 4 Pledged PLEOs;<br>7 Unpledged PLEOs</td></tr>
<tr><td class="tnb">34</td><td class="tnb"><a name="NJ"></a><a href="NJ-D">New Jersey</a></td><td class="tnb">153.0</td><td class="tnb">19.0</td><td class="tbb">172.0</td><td class="tnb">102 district / 34 at large; 17 Pledged PLEOs;<br>19 Unpledged PLEOs</td></tr>
<tr><td class="tna">35</td><td class="tna"><a name="NM"></a><a href="NM-D">New Mexico</a></td><td class="tna">39.0</td><td class="tna">11.0</td><td class="tba">50.0</td><td class="tna">26 district / 9 at large; 4 Pledged PLEOs;<br>11 Unpledged PLEOs</td></tr>
<tr><td class="tnb">36</td><td class="tnb"><a name="NY"></a><a href="NY-D">New York</a></td><td class="tnb">337.0</td><td class="tnb">47.0</td><td class="tbb">384.0</td><td class="tnb">226 district / 75 at large; 36 Pledged PLEOs;<br>47 Unpledged PLEOs</td></tr>
<tr><td class="tna">37</td><td class="tna"><a name="NC"></a><a href="NC-D">North Carolina</a></td><td class="tna">139.0</td><td class="tna">18.0</td><td class="tba">157.0</td><td class="tna">93 district / 31 at large; 15 Pledged PLEOs;<br>18 Unpledged PLEOs</td></tr>
<tr><td class="tnb">38</td><td class="tnb"><a name="ND"></a><a href="ND-D">North Dakota</a></td><td class="tnb">22.0</td><td class="tnb">5.0</td><td class="tbb">27.0</td><td class="tnb">15 district / 5 at large; 2 Pledged PLEOs;<br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">39</td><td class="tna"><a name="OH"></a><a href="OH-D">Ohio</a></td><td class="tna">174.0</td><td class="tna">17.0</td><td class="tba">191.0</td><td class="tna">113 district / 38 at large; 23 Pledged PLEOs;<br>17 Unpledged PLEOs</td></tr>
<tr><td class="tnb">40</td><td class="tnb"><a name="OK"></a><a href="OK-D">Oklahoma</a></td><td class="tnb">45.0</td><td class="tnb">5.0</td><td class="tbb">50.0</td><td class="tnb">29 district / 10 at large; 6 Pledged PLEOs;<br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">41</td><td class="tna"><a name="OR"></a><a href="OR-D">Oregon</a></td><td class="tna">70.0</td><td class="tna">14.0</td><td class="tba">84.0</td><td class="tna">47 district / 15 at large; 8 Pledged PLEOs;<br>14 Unpledged PLEOs</td></tr>
<tr><td class="tnb">42</td><td class="tnb"><a name="PA"></a><a href="PA-D">Pennsylvania</a></td><td class="tnb">228.0</td><td class="tnb">22.0</td><td class="tbb">250.0</td><td class="tnb">153 district / 51 at large; 24 Pledged PLEOs;<br>22 Unpledged PLEOs</td></tr>
<tr><td class="tna">43</td><td class="tna"><a name="PR"></a><a href="PR-D">Puerto Rico</a></td><td class="tna">60.0</td><td class="tna">7.0</td><td class="tba">67.0</td><td class="tna">40 district / 13 at large; 7 Pledged PLEOs;<br>7 Unpledged PLEOs</td></tr>
<tr><td class="tnb">44</td><td class="tnb"><a name="RI"></a><a href="RI-D">Rhode Island</a></td><td class="tnb">32.0</td><td class="tnb">8.0</td><td class="tbb">40.0</td><td class="tnb">22 district / 7 at large; 3 Pledged PLEOs;<br>8 Unpledged PLEOs</td></tr>
<tr><td class="tna">45</td><td class="tna"><a name="SC"></a><a href="SC-D">South Carolina</a></td><td class="tna">56.0</td><td class="tna">6.0</td><td class="tba">62.0</td><td class="tna">37 district / 12 at large; 7 Pledged PLEOs;<br>6 Unpledged PLEOs</td></tr>
<tr><td class="tnb">46</td><td class="tnb"><a name="SD"></a><a href="SD-D">South Dakota</a></td><td class="tnb">22.0</td><td class="tnb">7.0</td><td class="tbb">29.0</td><td class="tnb">15 district / 5 at large; 2 Pledged PLEOs;<br>7 Unpledged PLEOs</td></tr>
<tr><td class="tna">47</td><td class="tna"><a name="TN"></a><a href="TN-D">Tennessee</a></td><td class="tna">82.0</td><td class="tna">9.0</td><td class="tba">91.0</td><td class="tna">53 district / 18 at large; 11 Pledged PLEOs;<br>9 Unpledged PLEOs</td></tr>
<tr><td class="tnb">48</td><td class="tnb"><a name="TX"></a><a href="TX-D">Texas</a></td><td class="tnb">260.0</td><td class="tnb">27.0</td><td class="tbb">287.0</td><td class="tnb">172 district / 57 at large; 31 Pledged PLEOs;<br>27 Unpledged PLEOs</td></tr>
<tr><td class="tna">49</td><td class="tna"><a name="UN"></a><a href="UN-D">Unassigned</a></td><td class="tna">0.0</td><td class="tna">0.0</td><td class="tba">0.0</td><td class="tna">No delegate votes</td></tr>
<tr><td class="tnb">50</td><td class="tnb"><a name="UT"></a><a href="UT-D">Utah</a></td><td class="tnb">29.0</td><td class="tnb">5.0</td><td class="tbb">34.0</td><td class="tnb">19 district / 6 at large; 4 Pledged PLEOs;<br>5 Unpledged PLEOs</td></tr>
<tr><td class="tna">51</td><td class="tna"><a name="VT"></a><a href="VT-D">Vermont</a></td><td class="tna">18.0</td><td class="tna">9.0</td><td class="tba">27.0</td><td class="tna">12 district / 4 at large; 2 Pledged PLEOs;<br>9 Unpledged PLEOs</td></tr>
<tr><td class="tnb">52</td><td class="tnb"><a name="VI"></a><a href="VI-D">Virgin Islands</a></td><td class="tnb">7.0</td><td class="tnb">6.0</td><td class="tbb">13.0</td><td class="tnb">7 at large; <br>6 Unpledged PLEOs</td></tr>
<tr><td class="tna">53</td><td class="tna"><a name="VA"></a><a href="VA-D">Virginia</a></td><td class="tna">106.0</td><td class="tna">18.0</td><td class="tba">124.0</td><td class="tna">69 district / 23 at large; 14 Pledged PLEOs;<br>18 Unpledged PLEOs</td></tr>
<tr><td class="tnb">54</td><td class="tnb"><a name="WA"></a><a href="WA-D">Washington</a></td><td class="tnb">105.0</td><td class="tnb">15.0</td><td class="tbb">120.0</td><td class="tnb">69 district / 23 at large; 13 Pledged PLEOs;<br>15 Unpledged PLEOs</td></tr>
<tr><td class="tna">55</td><td class="tna"><a name="WV"></a><a href="WV-D">West Virginia</a></td><td class="tna">36.0</td><td class="tna">11.0</td><td class="tba">47.0</td><td class="tna">24 district / 8 at large; 4 Pledged PLEOs;<br>11 Unpledged PLEOs</td></tr>
<tr><td class="tnb">56</td><td class="tnb"><a name="WI"></a><a href="WI-D">Wisconsin</a></td><td class="tnb">100.0</td><td class="tnb">11.0</td><td class="tbb">111.0</td><td class="tnb">66 district / 22 at large; 12 Pledged PLEOs;<br>11 Unpledged PLEOs</td></tr>
<tr><td class="tna">57</td><td class="tna"><a name="WY"></a><a href="WY-D">Wyoming</a></td><td class="tna">18.0</td><td class="tna">4.0</td><td class="tba">22.0</td><td class="tna">12 district / 4 at large; 2 Pledged PLEOs;<br>4 Unpledged PLEOs</td></tr>
"""

stuff = stuff.replace("""<tr>""", " ");
stuff = stuff.replace("""<td>""", " ");
stuff = stuff.replace("""<td class="tba">""", "");
stuff = stuff.replace("""<td class="tna">""", ",");
stuff = stuff.replace("""<td class="tnb">""", ",");
stuff = stuff.replace("""<td class="tbb">""", ",");
stuff = stuff.replace("""</td>""", "");
stuff = stuff.replace("""</tr>""", "");
stuff = stuff.replace("""<a name=""", " ");
stuff = stuff.replace("""></a>""", "");
stuff = stuff.replace("""<a href=""", "  ");
stuff = stuff.replace("""</a>""", "  ");
stuff = stuff.replace("""<br>""", "  ");
stuff = stuff.replace(""">""", "  ");
#stuff = stuff.split("""\n""");


##SOURCE: http://www.thegreenpapers.com/P12/D-Del.phtml
##FORMAT (Example)
##41 district / 14 at large; 8 Pledged PLEOs;
##6 Unpledged PLEOs

print stuff
