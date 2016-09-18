#https://gist.github.com/pcchou/ace4dda397b8bf7bdfda
# M^e < N
fin =  17526664014799939674876416377135803518927961484240363149293761701887557441736929105230183755145952374519975399255138510937532377689709562995505193732891577744294631234368365056491598741057845686843042588398101554238608713670555538830766741882666988411302953426624744109729467897067579820913256206386166115777888570416263976382032093423457868881523186591757743035923815969999796147230136422551133209223757849315337360866828363273445934535167744456182109418825259957362850364400063033005281518923670724786281454305340951715217431282011728605135279975152409218204888813688669621614268119119410186605155734178230071786273447711357817965891029877836243826872266217105822784902199541344630109384192053091874226031670501862541877760926201407206277065127537875872299818550117110488445099430762295348639284852127263534388846983805602980849705725559547510372559302472028517840780158332973592425867850920448789756195813076005364758574737240360599909913651790477163691306365350495099181665043871132003528042787535692104193328475389557015250546252478479218281184929383836259750832268648646918936379380834953202154651467259310808171215343020875757003086211125439211939642562594342548645105941267160480083064597781872588302633807778432072108346773465450473165573153028250868537195865315514493666969095735676766023891389

def calc(x):
	return x**17

l = 0
r = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
m = 0
while l!=r:
	m = (l+r)//2
	v = calc(m)
	if v < fin :
		l = m
	elif fin < v :
		r = m
	else:
		break


print(m)
print hex(m)[2:-1].decode('hex')
