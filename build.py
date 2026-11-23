t=open('src/template.html').read()
for k,f in (('MODEL','model.js'),('DATA','data.js'),('APP','app.js')):
    t=t.replace('/*__%s__*/'%k, open('src/'+f).read().replace('</script>','<\\/script>'))
open('index.html','w').write(t)
print(len(t),'bytes')
