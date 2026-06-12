from django.shortcuts import render , redirect , get_object_or_404
from .models import Task


#              ADD     (add1 is also the home page)          #

def add_task(request):
    
    if request.method=="POST":

        value=request.POST.get ("item")
        
        
        if value:
            
            Task.objects.create(text=value)  
        return redirect("add_page")

    tasks=Task.objects.all()
    return render(request, 'todo_app/todo_app.html' , {"tasks":tasks})
             
            
 #             EDIT               #   
            

def edit_task(request):

    if request.method=="POST":

        edt_task=request.POST.get("new_edit")
        edt_id=request.POST.get("edit_it")

        if edt_task and edt_id:

            new_id=get_object_or_404(Task, id=edt_id) 
            new_id.text=edt_task
            new_id.save()
            

        return redirect("add_page")

   

    
#              DONE                #                
    

def check_task(request):
               
        if request.method=="POST":
            
            done_id=request.POST.get("complete")
            
                 
            if done_id:
                task_id=get_object_or_404(Task, id=done_id)
                task_id.done=True
                task_id.save()

               # tasks=Task.objects.all()

                                
                return redirect("add_page")



#                 UNDONE                 #
                
def undone_task(request):            
            
        if request.method=="POST":

            undone_id=request.POST.get("not_complete")

            if undone_id:
                undn_id=get_object_or_404(Task, id=undone_id)
                undn_id.done=False
                undn_id.save()    

            return redirect("add_page")



#                 DELETE                #

def delete_task(request):

    if request.method=="POST":

        del_task=request.POST.get("delete")

        if del_task:

            del_id=get_object_or_404(Task, id=del_task)
            del_id.delete()


        
        return redirect("add_page")


