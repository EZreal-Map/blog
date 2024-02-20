<template>
  <el-dialog v-model="userState.LoginVisibility" :width="dialogWidth">
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
        style="max-width: 300px"
        :model="userState"
        :rules="rules"
        ref="formRef"
      >
        <el-form-item label="Nickname" prop="Nickname">
          <el-input v-model="userState.Nickname" clearable />
        </el-form-item>
        <el-form-item label="Email" prop="Email">
          <el-input v-model="userState.Email" clearable />
        </el-form-item>
      </el-form>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="userState.LoginVisibility = false">Cancel</el-button>
        <el-button type="primary" @click="LoginConfirmHandle()"
          >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useUserStore } from '@/stores/user.js'
import { putUserEmailService } from '@/api/user.js'
import { ElMessage } from 'element-plus'

const userState = useUserStore()

const dialogWidth = computed(() => {
  // Calculate the width as 90% of the screen or 500px, whichever is smaller
  const screenWidth = window.innerWidth
  console.log('screenWidth:', screenWidth)
  return Math.min(screenWidth * 0.9, 500) + 'px'
})

let formRef = ref()
const rules = {
  Nickname: [{ required: true, message: '请输入昵称', trigger: 'blur' }],
  Email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    {
      type: 'email',
      message: '请输入有效的邮箱地址',
      trigger: ['blur', 'change']
    }
  ]
}

const LoginConfirmHandle = async () => {
  // await nextTick()
  // const valid = await formRef.value.validate()
  formRef.value
    .validate()
    .then(async () => {
      const message = await putUserEmailService(
        userState.Nickname,
        userState.Email
      )
      if (message.status === 200) {
        ElMessage({
          message: '登录成功',
          type: 'success'
        })
      }
      userState.LoginVisibility = false
    })
    .catch((err) => {
      for (const key in err) {
        ElMessage({
          message: err[key][0].message,
          type: 'error'
        })
      }
    })
}
</script>

<style scoped>
.login {
  padding: 0px 40px 0px 80px;
}

.title {
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: 700;
  text-align: center;
}

@media (max-width: 600px) {
  .login {
    padding: 0px 20px 0px 20px;
  }
  .title {
    margin-top: 0px;
    margin-bottom: 10px;
  }
}
</style>
