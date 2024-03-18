<template>
  <el-dialog v-model="userStore.LoginVisibility" :width="dialogWidth">
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
        :model="temp_model"
        :rules="rules"
        ref="formRef"
      >
        <el-form-item label="Nickname" prop="nickname">
          <el-input
            v-model="temp_model.nickname"
            placeholder="请输入昵称"
            clearable
          />
        </el-form-item>
        <el-form-item label="Email" prop="email">
          <el-input
            v-model="temp_model.email"
            placeholder="请输入邮箱"
            clearable
          />
        </el-form-item>
      </el-form>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="userStore.LogoutHandle()">登出</el-button>
        <el-button type="primary" @click="LoginConfirmHandle()">确定</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useUserStore } from '@/stores/user.js'
import { putUserEmailService } from '@/api/user.js'
// import { ElMessage } from 'element-plus'

const userStore = useUserStore()

const temp_model = ref({ nickname: userStore.Nickname, email: userStore.Email })

// 监视登录状态变化，更新昵称和邮箱
watch(
  () => userStore.LoginVisibility,
  () => {
    temp_model.value.nickname = userStore.Nickname
    temp_model.value.email = userStore.Email
  }
)

const dialogWidth = computed(() => {
  // Calculate the width as 90% of the screen or 500px, whichever is smaller
  const screenWidth = window.innerWidth
  return Math.min(screenWidth * 0.9, 500) + 'px'
})

let formRef = ref()
const rules = {
  nickname: [{ required: true, message: '请输入昵称', trigger: 'blur' }],
  email: [
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
        temp_model.value.nickname,
        temp_model.value.email
      )
      if (message.status === 200) {
        userStore.Role = message.data.role
        userStore.Nickname = message.data.nickname
        userStore.Email = message.data.email
        userStore.Token = message.data.token
        ElMessage({
          message: '登录成功',
          type: 'success'
        })
        userStore.LoginVisibility = false
      }
    })
    .catch((err) => {
      if (!err.isAxiosError) {
        // 处理其他错误, 如表单验证错误
        for (const key in err) {
          ElMessage({
            message: err[key][0].message,
            type: 'error'
          })
        }
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
