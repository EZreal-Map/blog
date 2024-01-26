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
        @click="dialogFormVisible = true"
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

    <el-dialog v-model="dialogFormVisible" width="500px">
      <div class="title">
        <el-popover
          placement="top"
          title="访客登录提醒"
          :width="300"
          trigger="hover"
          content="请使用个人邮箱填写，以确保下次登录时身份匹配正确。邮箱信息将保密，不公开显示。昵称随意填写和更改，将在公开显示时作为您的标识。祝您生活愉快！"
        >
          <template #reference>
            <span>登录/注册</span>
          </template>
        </el-popover>
      </div>
      <div class="login">
        <el-form
          label-position="top"
          label-width="100px"
          :model="formLabelAlign"
          style="max-width: 300px"
        >
          <el-form-item label="Nickname">
            <el-input v-model="formLabelAlign.Nickname" />
          </el-form-item>
          <el-form-item label="Email">
            <el-input v-model="formLabelAlign.Email" />
          </el-form-item>
        </el-form>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">
            Confirm
          </el-button>
        </span>
      </template>
    </el-dialog>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

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
const dialogFormVisible = ref(false)
const formLabelAlign = ref({
  Nickname: '',
  Email: ''
})
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

.pop-dialog {
  /* display: flex;
  justify-content: center;
  align-items: center; */
  width: 400px;
}

.login {
  padding: 0px 40px 0px 80px; /* 上右下左的顺时针顺序 */
}
.title {
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  /* background-color: red; */
}
</style>
