# project autyzmsoft_POM
Automatic tests of some functionalities of https://autyzmsoft.pl website
<p>
Most convenient usage:&nbsp;&nbsp;<em><strong>python3 suite_raport.py</strong></em><br>
Html reports are placed in <em>test_results</em> in the default directory
</p>

<h2>List of test cases:</h2>
Totals: 11 test cases<br>
<em>DP stands for Download Page test, HP - Home Page Tests, FV - Full Versions Page test</em>
<hr>
HP_01<br>
<strong>def test_download_page_appears(self):</strong><br>
        """ Fails if _verify_page() in DownloadPage class reports an error in its assert"""
<hr>
HP_02<br>
<strong>def test_full_versions_page_appears(self):</strong><br>
     """ Fails if _verify_page() in FullVersions class reports an error in its assert"""
<hr>
HP_03<br>
<strong>def test_all_links_are_active(self):</strong><br>
"""Checking whether all links on the Home Page are active."""<br>
<span style="color: red">Note: HP_03 is time-consuming</span>
<hr>
HP_04<br>
<strong>def test_liczykropka_js_opens(self):</strong>strong><br>
"""Test whether javascript application LiczyKropka opens"""<br>
"""Passed if:<br>
1. 5 buttons appear AND<br>
2. a big number appears<br>
"""<br>
<hr>
HP_05<br>
<strong>def test_profmarcin_js_opens(self):</strong>strong><br>
"""Test whether javascript application profMarcin opens"""<br>
"""Passed if:<br>
1. 4 buttons appear AND<br>
2. a picture appear<br>
"""<br>
<hr>
HP_06<br>
<strong>def test_clicking_correct_button_in_profmarcin_js(self):</strong><br>
"""Passed if:<br>
1. All texts on buttons with improper words are printed in 'font-weigh: normal'; text on button(s) with proper<br>
   word are printed in font-size > 100% AND<br>
2. There appear a text element under the picture. The element contains proper word AND<br>
3. Big green button with right arrow appears<br>
"""<br>
<hr>
HP_07<br>
<strong>def test_clicking_correct_button_in_liczykropka_js(self):</strong>strong><br>
"""Passed if:<br>
1. All buttons with numbers except the proper one(s) are disabled AND<br>
2. Big green button with @ sign appears<br>
"""<br>
<hr>
DP_01<br>
<strong>def test_getting_download_links_with_correct_email(self):</strong><br>
"""Passed if:<br>
1. Text "WYSLANO LINKI NA ADRES" appears AND<br>
2. Address email appears as text on the screen. The address is the same as the address given in the form.<br>
"""<br>
<hr>
DP_02<br>
<strong>def test_getting_download_links_with_incorrect_email(self):</strong><br>
"""Passed if:<br>
Text "We wprowadzonych danych wystąpiły błędy" appears<br>
"""<br>
<hr>
FV_01<br>
@data(1, 2)<br>
<strong>def test_click_order_buttons_without_choosing_items(self, button_number):</strong><br>
"""Passed if Alert window appears"""<br>
"""ddt is used as there are 2 buttons that clicking on them should have same effect"""<br>
<hr>
FV_02<br>
@data(1, 2)<br>
<strong>def test_click_order_buttons_after_choosing_items(self, button_number):</strong><br>
"""Passed if Order Details page appears"""<br>
"""ddt is used as there are 2 buttons that clicking on them should have same effect"""<br>
<p>&nbsp;</p>