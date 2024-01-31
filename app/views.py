from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1980)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__gt=7690)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='NEW YORK')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=5000)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[1:8:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__endswith='K')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__regex=r'JO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__contains='ALLEN')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def self_joins(request):
    empmgrobjcets=Emp.objects.select_related('mgr').all()
    empmgrobjcets=Emp.objects.select_related('mgr').filter(hiredate__year=1980)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(mgr__gt=7690)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(deptno=10)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(deptno__dlocation='NEW YORK')
    empmgrobjcets=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(deptno=20)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(deptno=30)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(sal__gt=500)
    empmgrobjcets=Emp.objects.select_related('mgr').filter(sal__lt=5000)
    empmgrobjcets=Emp.objects.select_related('mgr').all()[:5:]
    empmgrobjcets=Emp.objects.select_related('mgr').all()[2:5:]
    empmgrobjcets=Emp.objects.select_related('mgr').all()[1:8:]
    empmgrobjcets=Emp.objects.select_related('mgr').filter(ename__startswith='S')
    empmgrobjcets=Emp.objects.select_related('mgr').filter(ename__endswith='K')
    empmgrobjcets=Emp.objects.select_related('mgr').filter(ename__regex=r'JO')
    empmgrobjcets=Emp.objects.select_related('mgr').filter(ename__contains='ALLEN')
    empmgrobjcets=Emp.objects.select_related('mgr').all()
    
    d={'empmgrobjcets':empmgrobjcets}
    return render(request,'self_joins.html',d)
