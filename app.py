from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
tasks =[]
def save_tasks(tasks):
    with open ("tasks.txt","w",encoding="utf-8")as file:
        file.write("\n".join(tasks) )
def load_tasks():
    with open ("tasks.txt","r",encoding="utf-8")as file:
        tasks=[l.strip() for l in file.readlines()]
        return tasks
@app.route("/",methods=["GET","POST"])
def index():
    tasks=load_tasks()
    if request.method=="POST":
        task= request.form.get("task")
        if task:
            tasks.append(task)
            save_tasks(tasks)
    return render_template("index .html",tasks=tasks)
@app.route("/delete/<int:index>")
def delete_task(index):
    tasks=load_tasks()
    if 0 <=index<len(tasks):
        tasks.pop(index)
        save_tasks(tasks)


    return redirect(url_for("index"))
@app.route("/edit/<int:index>",methods=["GET","POST"])
def edit_task(index):
    tasks=load_tasks()
    if 0 >index or index>=len(tasks):
        return redirect(url_for("index"))
    if request.method=="POST":
        task=request.form.get("task")
        if task:
            tasks[index]=task
            save_tasks(tasks)
        return redirect(url_for("index"))
    task=tasks[index]
    return render_template(
        "edit.html",
        task=task,
        index=index

    )    



if __name__=="__main__":
    tasks=load_tasks()
    app.run(host="127.0.0.1",port=5000,debug=True)
