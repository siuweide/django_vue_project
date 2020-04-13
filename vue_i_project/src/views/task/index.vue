<template>
    <div class="task-main">
        <el-button @click="openAddTask">创建任务</el-button>

      <div class="task-list">
        <el-card class="task-card" v-for="item in taskList">
          <div slot="header" class="task-card-header">

            <div>
                {{item.name}}
            </div>
            <div>
                <el-button style="padding: 3px 0" type="text" @click="openEditTask(item)">编辑</el-button>
                <el-button style="padding: 3px 0; margin-left: 1px"
                           type="text" @click="deleteTaskFun(item.id)">删除</el-button>
            </div>
          </div>
          <div>
            {{item.description}}
          </div>
        </el-card>
      </div>

        <el-dialog title="创建任务" :visible.sync="dialogAddVisible">
        <el-form ref="addFormRef" :model="addForm" :rules="addRules" label-width="50px">
            <el-form-item label="名称" prop="name">
              <el-input v-model="addForm.name"></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="description">
              <el-input type="textarea" v-model="addForm.description"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogAddVisible = false">取 消</el-button>
            <el-button type="primary" @click="addTaskFun" >确 定</el-button>
          </div>
        </el-dialog>

        <el-dialog title="编辑任务" :visible.sync="dialogEditVisible">
          <el-form ref="editFormRef" :model="editForm" :rules="editRules" label-width="50px">
            <el-form-item label="名称" prop="name">
              <el-input v-model="editForm.name"></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="description">
              <el-input type="textarea" v-model="editForm.description"></el-input>
            </el-form-item>
            </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogEditVisible = false">取 消</el-button>
            <el-button type="primary" @click="editTaskFun" >确 定</el-button>
          </div>
        </el-dialog>
    </div>
</template>

<script>
  import {addTask, deleteTask, getAllTasks, updateTask} from "../../../request/task";

    export default {
        name: "index",
        data(){
            return {
                dialogAddVisible: false,
                dialogEditVisible: false,
                addForm : {
                    name: "",
                    description: "",
                },
                addRules: {
                    name: [
                        { required: true, message: '请输入名称', trigger: 'blur' },
                      ],
                    description: [
                        { required: true, message: '请输入描述', trigger: 'blur' }
                    ],
                },
                editForm : {
                    id: 0,
                    name: "",
                    description: "",
                },
                editRules: {
                    name: [
                        { required: true, message: '请输入名称', trigger: 'blur' },
                      ],
                    description: [
                        { required: true, message: '请输入描述', trigger: 'blur' }
                    ]
                },
                taskList: []
            }
        },
        created() {
            this.getAllTasksFun()
        },
        methods: {
            deleteTaskFun(TaskId) {
              this.$confirm('此操作将永久删除该任务, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
              }).then(() => {
                    // 点击确定
                    deleteTask(TaskId).then(data => {
                        let success = data.data.success;
                        if (success) {
                            this.getAllTasksFun()
                        }else {
                            this.$notify.error({
                                title: '错误',
                                message: '请求失败',
                            })
                        }
                    })
              }).catch(() => {
                    // 点击取消
              });
            },
            getAllTasksFun(){
                getAllTasks().then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.taskList = data.data.data
                    }else {
                        this.$notify.error({
                            title: '错误' ,
                            message: '请求失败',
                        })
                    }
                })
            },
            openAddTask(){ // 这是打开创建任务
                this.dialogAddVisible = true
            },
            addTaskFun(){ // 这是确定创建任务
                this.$refs.addFormRef.validate((valid) => {
                  if (valid) {
                    // 表单检验通过
                    addTask(this.addForm).then(data=> {
                        let success = data.data.success;
                        if (success) {
                            this.dialogAddVisible = false;
                            this.getAllTasksFun()
                        }else {
                            this.$notify.error({
                                title: '错误' ,
                                message: '请求失败',
                            })
                        }
                    })
                  } else {
                    console.log('error submit!!');
                    return false;
                  }
                });
            },
            openEditTask(data){ // 这是打开编辑任务
                this.dialogEditVisible = true;
                this.editForm.id = data.id;
                this.editForm.name = data.name;
                this.editForm.description = data.description
            },
            editTaskFun(){ // 这是确定编辑任务
                this.$refs.editFormRef.validate((valid) => {
                  if (valid) {
                    // 表单检验通过
                    updateTask(this.editForm.id, this.editForm).then(data=> {
                        let success = data.data.success;
                        if (success) {
                            this.dialogEditVisible = false;
                            this.getAllTasksFun()
                        }else {
                            this.$notify.error({
                                title: '错误' ,
                                message: '请求失败',
                            })
                        }
                    })
                  } else {
                    console.log('error submit!!');
                    return false;
                  }
                });
              },
        }
    }
</script>

<style scoped>
    .task-main {
        text-align: left;
        padding-top: 5px;
        padding-left: 5px;
    }
    .task-card {
        width: 30%;
        margin-top: 10px;
        margin-right: 10px;;
    }
    .task-list {
        display: flex;
        flex-wrap: wrap;
    }

    .task-card-header {
      display: flex;
      justify-content: space-between;
    }
</style>
