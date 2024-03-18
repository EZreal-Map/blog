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
      index="/blog/categories"
      @click="router.push({ path: '/blog/categories' })"
      >分类</el-menu-item
    >
    <!-- 总结占格子，作用撑开的作用 -->
    <div class="flex-grow"></div>
    <el-sub-menu index="admin" popper-class="pop-menu">
      <template #title>{{ userStore.Nickname || 'VISITOR' }}</template>
      <el-menu-item
        class="submenu-paddingleft"
        index="login"
        @click="userStore.LoginVisibility = true"
        >登录</el-menu-item
      >
      <!-- 如果不是管理员，则禁用删除按钮 -->
      <el-menu-item
        class="submenu-paddingleft"
        index="/blog/create"
        @click="router.push({ path: '/blog/create' })"
        :disabled="userStore.Role !== 'admin'"
        >新建</el-menu-item
      >
      <!-- 如果不是管理员或者编辑按钮被禁用，则禁用删除按钮 -->
      <el-menu-item
        class="submenu-paddingleft"
        index="/blog/delete"
        @click="deleteBlogHandle()"
        :disabled="userStore.Role !== 'admin' || userStore.EditIconDisabled"
        >删除</el-menu-item
      >
      <!-- 如果不是管理员或者编辑按钮被禁用，则禁用编辑按钮 -->
      <el-menu-item
        class="submenu-paddingleft"
        index="edit"
        @click="userStore.Edit = !userStore.Edit"
        :disabled="userStore.Role !== 'admin' || userStore.EditIconDisabled"
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
// import { ElMessage, ElMessageBox } from 'element-plus'
import { deleteBlogIDService } from '@/api/blog'

const userStore = useUserStore()

const route = useRoute()
const router = useRouter()

const deleteBlogHandle = () => {
  const blogId = route.params.id
//   console.log('deleteBlogHandle', blogId)
  ElMessageBox.confirm('确定要删除这篇博客吗？', '警告', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  })
    .then(() => {
      ElMessage({
        type: 'success',
        message: '删除成功'
      })
      deleteBlogIDService(blogId)
      router.push({ path: '/blog/articles' })
      // 等待一小段时间，然后重新加载页面
      setTimeout(() => {
        window.location.reload()
      }, 0) // 适当的等待时间，确保路由生效
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '取消删除'
      })
    })
}
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
