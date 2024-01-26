<template>
  <div class="main">
    <div class="login">
      <el-popover
        placement="top-start"
        title="访客登录提醒"
        :width="300"
        trigger="hover"
        content="请使用个人邮箱填写，以确保下次登录时身份匹配正确。邮箱信息将保密，不公开显示。昵称随意填写和更改，将在公开显示时作为您的标识。祝您生活愉快！"
      >
        <template #reference>
          <div class="title">登录/注册</div>
        </template>
      </el-popover>
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
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Create</el-button>
          <el-button>Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const formLabelAlign = ref({
  Nickname: '',
  Email: ''
})
</script>

<style scoped>
.main {
  display: flex;
  justify-content: center;
  align-items: center;
}

.login {
  background-color: white;
  padding: 40px 50px 20px 40px; /* 上右下左的顺时针顺序 */
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 300px; /* 调整 max-width */
  width: 100%; /* 让它充满整个容器宽度 */
}
.login .title {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  /* background-color: red; */
}
</style>
