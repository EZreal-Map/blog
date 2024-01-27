<template>
  <el-menu
    :default-active="activeRoute"
    mode="horizontal"
    :ellipsis="false"
    :router="true"
    class="header-font-weight"
  >
    <el-menu-item index="/blog/home">首页</el-menu-item>
    <el-menu-item index="/blog/articles">时间归档</el-menu-item>
    <el-menu-item index="/blog/catogory">分类</el-menu-item>
    <div class="flex-grow" />
    <el-sub-menu :index="activeRoute" popper-class="pop-menu">
      <template #title>Admin</template>
      <el-menu-item
        :index="activeRoute"
        class="submenu-paddingleft"
        @click="userState.LoginVisibility = true"
        >登录</el-menu-item
      >
      <el-menu-item :index="activeRoute" class="submenu-paddingleft"
        >新建</el-menu-item
      >
      <el-menu-item :index="activeRoute" class="submenu-paddingleft"
        >查看</el-menu-item
      >
      <el-menu-item :index="activeRoute" class="submenu-paddingleft"
        >编辑</el-menu-item
      >
    </el-sub-menu>
    <LoginView> </LoginView>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue'
import LoginView from '@/components/LoginView.vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user.js'
const userState = useUserStore()

const route = useRoute()
const activeRoute = ref('')
watch(
  () => route.path,
  (newVal) => {
    activeRoute.value = newVal
  }
)

//   const handleSelect = (key: string, keyPath: string[]) => {
//     console.log(key, keyPath)
//   }
</script>

<style>
/* 为了设置submenu文字居中，加了padding-left，这里的样式是全局的，不是局部的 scoped还不能加 */
.flex-grow {
  flex-grow: 1;
}

.header-font-weight {
  font-weight: 700;
}
.pop-menu {
  overflow: hidden;
  width: 100px; /* 设置固定宽度，可以根据需要调整 */
}

.submenu-paddingleft {
  padding-left: 35px !important; /* 设置固定宽度，可以根据需要调整 */
}
</style>
