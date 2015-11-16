<h1> DSP Test 3: </h1>

Two Problems
  <ol>
    <li> allpass minimum phase, and generalize liner phase filters</li>
    <li> design of IIR filtering using bilinear transform</li>
  </ol>
Test will cover the following sections

  * 5.5-5.7
  * 7.1-7.2
  * Appendix B

<h2>Book Notes:</h2>

<h4>Section 5-5 -- *All Pass Systems* -- </h4>
H<sub>ap</sub>(z) = &nbsp;&nbsp;
                    <sup>z<sup>-1</sup>-a<sup> * </sup></sup>
                    &nbsp;&#8725;&nbsp;
                    <sub>1-az<sup>-1</sup></sub><br><br>
H<sub>ap</sub>(e<sup>j&omega;</sup>)= &nbsp;&nbsp;
                                e<sup>-j&omega;</sup> * (<sup>1-a<sup> * </sup>
                                e<sup>j&omega;</sup></sup>
                                &nbsp;&#8725;&nbsp;
                                <sub>1-ae<sup>-j&omega;</sup></sub>
                                )<br><br>
<img src=allpass_pz.png>
<p>
  <ul>
  <li>complex conjugate pole and zero magnitude is 1 for all &omega;</li>
  <li> used as compensator for phase  or group delay distortion</li>
  <li> useful for minimum-phase theory
  </ul>
<u>causal All Pass properties:</u><ul><ul>
    <li> positive group delay</li>
    <li> negative unwrapped phase</li>
  </ul></ul>
</p>



<h4>Section 5-6: -- *Minimum Phase Systems* -- </h4>
<ul><u>
Recall Sec 5.4: Magnitude/Phase Relationship</u><ul>
    <li> There is no relationship between magnitude and phase except
         for Rational System Functions </li><ul>
         <li> <u>Rational System Function:</u> &nbsp; Linear constant coefficient differential equation </li> </ul>
    <li> freq-resp magnitude for LTI system with rational function does not uniquely characterize the system  </li>
    <li> stable and causal if poles are inside the unit circle </li>
    <li> no restriction on the zeros </li>
    <li> if the Magnitude, poles and zeros are known --> only finite number of choices for associated phase</li>
    <li> if the Phase, poles and zeros are known --> only finite number of choices for associated Magnitudes</li>
    <li> |H(e<sup>j&omega;</sup>)|<sup>2</sup> = H(e<sup>j&omega;</sup>) &sdot; H<sup>&lowast;</sup>(e<sup>j&omega;</sup>) = H(z) &sdot; h<sup>&lowast;</sup>(1/ z*) |<sub>z=ej&omega;
    </ul>
</ul>
<ul><u>
Minimum Phase System:</u> <ul>
    <li> H(z) must be stable and causal</li>
    <li> <sup>1</sup> &frasl; <sub>H(z)</sub>&nbsp; must also be stable and causal</li>
    <li> both poles and zeros must be in the unit circle </li>
    <li> properties of minimum-phase are in 5.6.3 </li>
    <li> non-minimum phase --> minimum-phase</li><ul>
      <li>reflect all zeros lying outside the unit circle to their conjugate reciprocal positions inside the unit circle</li></ul>
      </ul>
</ul>

------------------------------------------------

<h4>Subject Notes:</h4><hr>
<u>FIR filters:</u><ul>
  <li> book pg 363, pdf pg 392
  </li>
  <li> 4 types of filters
  </li>
  <li>how do we use poles/zeros
  </li>
</ul>
allpass notes:

minimum phase notes:

<u>generalize linear phase filters:
</u>

| Type I         | Type II        | Type III       | Type IV        |
| :------------- | :------------- | :------------- | :------------- |
| Item One       | Item Two       | Item One       | Item Two       |


group delay:

order:

how/why/when are we going between discrete time and continuous time:



lablace domain:
  * stability
  * causality
  * transform
  * zeros
    * conjugates
    * what can we say about this
