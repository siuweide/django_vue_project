<template>
    <div class="home">
        <div class="left-menu">
            <el-menu
                    style="height: 100%;"
                    :default-active="activeIndex"
                    class="el-menu-vertical-demo"
                    background-color="#304156"
                    active-text-color="#409eff"
                    @select="handleSelect"
                    text-color="#fff">

                        <el-menu-item index="service" style="text-align: left">
                            <i class="el-icon-menu"></i>
                            <span slot="title">服务</span>
                        </el-menu-item>
                        <el-menu-item index="interface" style="text-align: left">
                            <i class="el-icon-star-on"></i>
                            <span slot="title">接口</span>
                        </el-menu-item>
                        <el-menu-item index="task" style="text-align: left">
                            <i class="el-icon-setting"></i>
                            <span slot="title">任务</span>
                        </el-menu-item>
                        <el-menu-item index="logout" style="text-align: left">
                            <i class="el-icon-user"></i>
                            <span slot="title">退出登录</span>
                        </el-menu-item>
            </el-menu>
        </div>
        <div class="right-context">
            <router-view/>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import {logout} from "../../request/user";

    export default {
        name: 'home',
        components: {},
        props: {
            menu: String,
        },
        data() {
            return {
                activeIndex: "service",
            }
        },
        methods: {
            logoutUser(){
                logout().then(data => {
                    let success = data.data.success;
                    if (success) {
                        this.$router.push('/login')
                    } else {
                        this.$notify.error({
                            title: '错误',
                            message: '请求失败'
                        })
                    }
                });
            },
            handleSelect(index, keyPath) {
                switch (index) {
                    case "logout":
                        this.logoutUser();
                        break;
                    case "service":
                        this.$router.push('service');
                        break;
                    case "interface":
                        this.$router.push('interface');
                        break;
                    case "task":
                        this.$router.push('task');
                        break;
                }
          }
        },
        created() {
            this.activeIndex = this.menu
        },
    }
</script>

<style scoped>
    .home {
        display: flex;
        height: 100%;
    }
    .left-menu {
        width: 15%;
    }
    .right-context {
        width: 85%;
    }
</style>
