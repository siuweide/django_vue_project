<template>
    <div class="main-list">
        <el-select v-model="serviceId" placeholder="请选择" @change="changeSelectService">
                <el-option
                  v-for="item in serviceList"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id">
                </el-option>
        </el-select>

        <div class="interface-list">
            <el-table
                    @selection-change="handleSelectionChange"
                    :data="interfaceList"
                    stripe
                    style="width: 100%; max-height: 600px; overflow: auto">
                <el-table-column
                  type="selection"
                  width="%5">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="名称"
                        min-width="45%">
                </el-table-column>
                <el-table-column
                        label="URL"
                        min-width="50%">
                    <template slot-scope="scope">
                        {{scope.row.context.url}}
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
    import {getAllServices} from "../../../request/service";
    import {getInterfaces} from "../../../request/interface";

    export default {
        name: "selectInterface",
        data() {
            return {
                serviceId: undefined,
                serviceList: [],
                interfaceList: [],

                multipleSelection: [],
            }
        },
        methods: {
            changeSelectService(serviceId){
                this.getInterfacesFun(serviceId)
            },
            getInterfacesFun(serviceId) {
                getInterfaces(serviceId).then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.interfaceList = data.data.data;
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        });
                    }
                })
            },
            handleSelectionChange(val) {  // 点击选择框的回调，把所有已选择的数据都返回过来
                this.multipleSelection = val
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
        },
        created() {
            this.getAllServicesFun()
        }
    }
</script>

<style scoped>
    .main-list {
        display: flex;
    }
    .service-list {
        width: 20%;
        padding: 5px;
    }
    .interface-list {
        width: 100%;
        padding: 5px;
    }
    .service-item {
        font-size: 18px;
        padding: 10px 0 5px  5px;
    }
</style>
