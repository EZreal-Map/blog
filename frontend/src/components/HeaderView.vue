<template>
  <el-menu
    :default-active="route.path"
    mode="horizontal"
    :ellipsis="false"
    :router="false"
    class="header-font-weight"
  >
    <!-- 这里不使用el-menu默认router，灵活度不够，不能指定哪些跳转和哪些不跳转 -->
    <el-menu-item
      index="/blog/home"
      @click="router.push({ path: '/blog/home' })"
      >首页</el-menu-item
    >
    <el-menu-item
      index="/blog/articles"
      @click="router.push({ path: '/blog/articles' })"
      >时间归档</el-menu-item
    >
    <el-menu-item
      index="/blog/category"
      @click="router.push({ path: '/blog/categories' })"
      >分类</el-menu-item
    >
    <div class="flex-grow" />
    <el-sub-menu index="admin" popper-class="pop-menu">
      <template #title>Admin</template>
      <el-menu-item
        class="submenu-paddingleft"
        index="login"
        @click="userState.LoginVisibility = true"
        >登录</el-menu-item
      >
      <el-menu-item
        class="submenu-paddingleft"
        index="/blog/create"
        @click="router.push({ path: '/blog/create' })"
        >新建</el-menu-item
      >
      <el-menu-item
        class="submenu-paddingleft"
        index="/blog/create"
        @click="router.push({ path: '/blog' })"
        >删除</el-menu-item
      >
      <el-menu-item
        class="submenu-paddingleft"
        index="edit"
        @click="userState.Edit = !userState.Edit"
        :disabled="userState.EditIconDisabled"
        >编辑</el-menu-item
      >
    </el-sub-menu>
    <LoginView> </LoginView>
  </el-menu>
</template>

<script lang="ts" setup>
import LoginView from '@/components/LoginView.vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user.js'
const userState = useUserStore()

const route = useRoute()
const router = useRouter()
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
