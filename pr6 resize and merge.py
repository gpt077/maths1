def RESIZE(Im_1,m,n):
    from PIL import Image
    a1 =Image.open(Im_1)
    a1.show()
    new_a1=a1.resize((m,n))
    new_a1.save('path here')
    new_a1.show()

def MERGE(IM_1,IM_2,a,b):
    from PIL import Image
    import numpy as np
    a1=Image.open(IM_1)
    a2=Image.open(IM_2)
    a1.show()
    a2.show()
    new_a1=a1.resize((300,300))
    new_a2=a2.resize((300,300))
    p=a*np.array(new_a1)+b*np.array(new_a2)
    a=Image.fromarray(p)
    a.save('path here')
    a.show()
    print(np.array(a))
