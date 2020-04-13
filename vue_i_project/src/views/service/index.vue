<template>
    <div class="service-main">
        <el-button @click="openAddModel">创建服务</el-button>

      <div class="service-list">
        <el-card class="service-card" v-for="item in serviceList">
          <div slot="header" class="service-card-header">

            <div>
                {{item.name}}
            </div>
            <div>
                <el-button style="padding: 3px 0" type="text" @click="openEditModel(item)">编辑</el-button>
                <el-button style="padding: 3px 0; margin-left: 1px"
                           type="text" @click="deleteServiceFun(item.id)">删除</el-button>
            </div>
          </div>
          <div>
            {{item.description}}
          </div>
        </el-card>
      </div>

        <el-dialog title="创建服务" :visible.sync="dialogAddVisible">
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
            <el-button type="primary" @click="addServiceFun" >确 定</el-button>
          </div>
        </el-dialog>

        <el-dialog title="编辑服务" :visible.sync="dialogEditVisible">
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
            <el-button type="primary" @click="editServiceFun" >确 定</el-button>
          </div>
        </el-dialog>
    </div>
</template>

<script>
  import {addService, deleteService, getAllServices, updateService} from "../../../request/service";

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
                serviceList: []
            }
        },
        created() {
            this.getAllServicesFun()  // 初始化函数
        },
        methods: {
            deleteServiceFun(serviceId) {
              this.$confirm('此操作将永久删除该服务, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
              }).then(() => {
                    // 点击确定
                    deleteService(serviceId).then(data => {
                        let success = data.data.success;
                        if (success) {
                            this.getAllServicesFun()
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
            getAllServicesFun(){ // 获取所有服务
                getAllServices().then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.serviceList = data.data.data
                    }else {
                        this.$notify.error({
                            title: '错误' ,
                            message: '请求失败',
                        })
                    }
                })
            },
            openAddModel(){ // 这是打开创建服务
                this.dialogAddVisible = true
            },
            addServiceFun(){ // 这是确定创建服务
                this.$refs.addFormRef.validate((valid) => {
                  if (valid) {
                    // 表单检验通过
                    addService(this.addForm).then(data=> {
                        let success = data.data.success;
                        if (success) {
                            this.dialogAddVisible = false;
                            this.getAllServicesFun()
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
            openEditModel(data){ // 这是打开编辑服务
                this.dialogEditVisible = true;
                this.editForm.id = data.id;
                this.editForm.name = data.name;
                this.editForm.description = data.description
            },
            editServiceFun(){ // 这是确定编辑服务
                this.$refs.editFormRef.validate((valid) => {
                  if (valid) {
                    // 表单检验通过
                    updateService(this.editForm.id, this.editForm).then(data=> {
                        let success = data.data.success;
                        if (success) {
                            this.dialogEditVisible = false;
                            this.getAllServicesFun()
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
    .service-main {
        text-align: left;
        padding-top: 5px;
        padding-left: 5px;
    }
    .service-card {
        width: 30%;
        margin-top: 10px;
        margin-right: 10px;;
    }
    .service-list {
        display: flex;
        flex-wrap: wrap;
    }

    .service-card-header {
      display: flex;
      justify-content: space-between;
    }
</style>
