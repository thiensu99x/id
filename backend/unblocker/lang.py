class zh_cn:
    def __init__(self):
        self.ErrorRetrievingConfig = "获取配置失败"
        self.launch = "启动AppleID_Auto"
        self.failOnPasswordUpdate = "更新密码失败"
        self.failOnRetrievingPassword = "获取密码失败"
        self.failOnMessageUpdate = "更新消息失败"
        self.failOnReportingProxyError = "上报代理错误失败"
        self.failOnRetrievingProxyFromAPI = "从API获取代理失败"
        self.retrievedProxyFromAPI = "从API获取到代理"
        self.backgroundRunning = "已启用 后台运行"
        self.removeDevice = "已启用 删除设备"
        self.checkPassword = "已启用 检查密码"
        self.autoUpdatePassword = "已启用 定时更新密码"
        self.usingProxyID = "使用代理ID"
        self.failOnRefreshingPage = "刷新页面失败"
        self.proxyEnabledRefreshing = "已启用代理，请检查代理是否可用"
        self.proxyEnabledRefreshingAPI = "页面加载失败，可能是代理不可用"
        self.failOnLoadingPage = "页面加载失败"
        self.IPBlocked = "页面加载失败，疑似服务器IP被封禁"
        self.seeLog = "页面加载失败，具体原因请查看日志"
        self.failOnGettingCaptcha = "无法获取验证码"
        self.failOnRetrievingPage = "无法获取页面内容，即将退出程序"
        self.proxyEnabledGettingContent = "无法获取页面内容，可能是代理不可用"
        self.failOnGettingPage = "无法获取页面内容"
        self.captchaCorrect = "验证码正确"
        self.captchaFail = "验证码错误，重新输入"
        self.login = "登录成功"
        self.loginFail = "登陆失败"
        self.blocked = "无法处理请求，可能是账号失效或服务器IP被拉黑"
        self.loginFailCheckLog = "解锁登录失败，可能是账号失效或服务器IP被拉黑，具体请查看后端日志"
        self.notLocked = "当前账号未被锁定"
        self.locked = "当前账号已被锁定"
        self.twoStepnotEnabled = "当前账号未开启2FA"
        self.twoStepEnabled = "当前账号已开启2FA"
        self.cantFindDisable2FA = "关闭二步验证失败，可能是账号不允许关闭2FA"
        self.rejectedByApple = "操作被苹果拒绝，疑似被风控"
        self.chooseFail = "选择选项失败，无法使用安全问题解锁"
        self.loginLoadFail = "登录页面加载失败"
        self.answerIncorrect = "安全问题错误，程序已退出"
        self.answerNotMatch = "未找到安全问题对应答案，请检查配置"
        self.failOnBypass2FA = "跳过双重验证失败"
        self.startRemoving = "开始删除设备"
        self.noRemoveRequired = "没有设备需要删除"
        self.finishRemoving = "设备删除完毕"
        self.DOB_Error = "安全问题获取失败，可能是生日错误"
        self.failOnAnswer = "安全问题答案错误"
        self.passwordNotFound = "密码框获取失败"
        self.unknownError = "执行任务时遇到未知错误"
        self.passwordUpdated = "密码修改成功，新密码为"
        self.startChangePassword = "开始修改密码"
        self.failOnChangePassword = "现在无法修改密码，可能是二步验证关闭失败"
        self.failToUseSecurityQuestion = "无法使用安全问题重设密码，修改失败"
        self.TGFail = "Telegram发送消息失败"
        self.cnTG = "如果机器在中国大陆，请勿开启Telegram通知"
        self.failOnCallingWD = "Webdriver调用失败"
        self.twoStepDetected = "检测到账号开启双重认证，开始解锁"
        self.accountLocked = "检测到账号被锁定，开始解锁"
        self.updateSuccess = "Apple ID更新成功"
        self.newPassword = "新密码: "
        self.passwordChanged = "密码错误，开始修改密码"
        self.LoginFail = "登录Apple ID失败，无法删除设备"
        self.missionFailed = "任务执行失败，等待下次检测"
        self.WDCloseError = "Webdriver关闭失败"
        self.repoAddress = "项目地址"
        self.TG_Group = "Telegram交流群"
        self.version = "当前版本"
        self.UnlockFail = "解锁失败"
        self.FailToChangePassword = "修改密码失败"
        self.CurrentAccount = "当前账号："
        self.invalidProxyType = "无效的代理类型"
        self.failOnSavingScreenshot = "无法保存错误页面截图"
        self.screenshotSaved = "已保存错误页面到/app目录下error.html和error.png，请与开发者反馈"
        self.getIPFail = "无法获取当前IP"
        self.updateFail = "更新账号失败"
        self.getAPIFail = "从API获取配置失败"
        self.checkComplete = "账号检测完毕"

    def nextRun(self, time):
        return f"下次任务将在{time}分钟后执行"

    def totalDevices(self, total):
        return f"共有{total}个设备"


class en_us:
    def __init__(self):
        self.ErrorRetrievingConfig = "Error retrieving config"
        self.launch = "Launch AppleID_Auto"
        self.failOnPasswordUpdate = "Password update failed"
        self.failOnRetrievingPassword = "Retrieving password failed"
        self.failOnMessageUpdate = "Message update failed"
        self.failOnReportingProxyError = "Reporting proxy error failed"
        self.failOnRetrievingProxyFromAPI = "Retrieving proxy from API failed"
        self.retrievedProxyFromAPI = "Retrieved proxy from API"
        self.backgroundRunning = "Background running enabled"
        self.removeDevice = "Remove device enabled"
        self.checkPassword = "Check password enabled"
        self.autoUpdatePassword = "Auto update password enabled"
        self.UsingProxyID = "Using proxy ID"
        self.failOnRefreshingPage = "Refreshing page failed"
        self.proxyEnabledRefreshing = "Proxy is enabled, please check the availability of proxy"
        self.proxyEnabledRefreshingAPI = "Page loading failed, proxy may not be available"
        self.failOnLoadingPage = "Page loading failed"
        self.IPBlocked = "Page loading failed, the server IP may be blocked"
        self.seeLog = "Page loading failed, please check the log for details"
        self.failOnGettingCaptcha = "Failed to get captcha"
        self.failOnRetrievingPage = "Failed to retrieve page content, exiting"
        self.proxyEnabledGettingContent = "Failed to retrieve page content, proxy may not be available"
        self.failOnGettingPage = "Failed to retrieve page content"
        self.captchaCorrect = "Captcha correct"
        self.captchaFail = "Captcha incorrect, please try again"
        self.login = "Login successful"
        self.loginFail = "Login failed"
        self.blocked = "Unable to process request, account may be invalid or server IP may be blocked"
        self.loginFailCheckLog = "Login failed, account may be invalid or server IP may be blocked, " \
                                 "please check the backend log for details"
        self.notLocked = "Account is not locked"
        self.locked = "Account is locked"
        self.twoStepnotEnabled = "2FA is not enabled"
        self.twoStepEnabled = "2FA is enabled"
        self.cantFindDisable2FA = "Failed to disable 2FA, account may not allow 2FA to be disabled"
        self.rejectedByApple = "Action rejected by Apple, suspected of being under risk control"
        self.chooseFail = "Failed to choose option, unable to unlock by security questions"
        self.loginLoadFail = "Login page loading failed"
        self.answerIncorrect = "Security question answer incorrect, program exited"
        self.answerNotMatch = "Answers for security questions not found, please check the config"
        self.failOnBypass2FA = "Failed to bypass 2FA"
        self.startRemoving = "Start removing device"
        self.noRemoveRequired = "No device to remove"
        self.finishRemoving = "Device removal complete"
        self.DOB_Error = "Failed to get security question, birthday may be incorrect"
        self.failOnAnswer = "Security question answer incorrect"
        self.passwordNotFound = "Password box not found"
        self.unknownError = "An unknown error was encountered while executing the task"
        self.passwordUpdated = "Password updated, new password is "
        self.startChangePassword = "Start changing password"
        self.failOnChangePassword = "Unable to change password now, 2FA may not be disabled"
        self.failToUseSecurityQuestion = "Unable to use security question to reset password, password change failed"
        self.TGFail = "Telegram message sending failed"
        self.cnTG = "If your server is located in mainland China, please do not enable Telegram notification"
        self.failOnCallingWD = "Webdriver calling failed"
        self.twoStepDetected = "2FA is enabled, start unlocking"
        self.accountLocked = "Account is locked, start unlocking"
        self.updateSuccess = "Apple ID updated successfully"
        self.newPassword = "New password: "
        self.passwordChanged = "Password incorrect, start changing password"
        self.LoginFail = "Login Apple ID failed, unable to remove device"
        self.missionFailed = "Mission failed, waiting for next check"
        self.WDCloseError = "Webdriver close failed"
        self.repoAddress = "Project repo address"
        self.TG_Group = "Telegram group"
        self.version = "Current version"
        self.UnlockFail = "Failed to unlock"
        self.FailToChangePassword = "Failed to change password"
        self.CurrentAccount = "Current account:"
        self.invalidProxyType = "Invalid proxy type"
        self.failOnSavingScreenshot = "Unable to save screenshot of error page"
        self.screenshotSaved = "Screenshot of error page saved to /app/error.html and /app/error.png, " \
                               "please contact the developer"
        self.getIPFail = "Unable to get current IP"
        self.updateFail = "Update account failed"
        self.getAPIFail = "Failed to get config from API"
        self.checkComplete = "Account check complete"
        
    def nextRun(self, time):
        return f"Next job will be executed in {time} minutes"

    def totalDevices(self, total):
        return f"{total} devices in total"
        
class vi_vn:
    def __init__(self):
        self.ErrorRetrievingConfig = "Lỗi khi truy xuất cấu hình"
        self.launch = "Khởi động AppleID_Auto"
        self.failOnPasswordUpdate = "Cập nhật mật khẩu thất bại"
        self.failOnRetrievingPassword = "Lấy mật khẩu thất bại"
        self.failOnMessageUpdate = "Cập nhật tin nhắn thất bại"
        self.failOnReportingProxyError = "Báo lỗi proxy thất bại"
        self.failOnRetrievingProxyFromAPI = "Lấy proxy từ API thất bại"
        self.retrievedProxyFromAPI = "Đã lấy proxy từ API"
        self.backgroundRunning = "Chế độ chạy nền đã được kích hoạt"
        self.removeDevice = "Chế độ xóa thiết bị đã được kích hoạt"
        self.checkPassword = "Chế độ kiểm tra mật khẩu đã được kích hoạt"
        self.autoUpdatePassword = "Chế độ tự động cập nhật mật khẩu đã được kích hoạt"
        self.UsingProxyID = "Đang sử dụng proxy ID"
        self.failOnRefreshingPage = "Làm mới trang thất bại"
        self.proxyEnabledRefreshing = "Proxy đã được kích hoạt, vui lòng kiểm tra tính khả dụng của proxy"
        self.proxyEnabledRefreshingAPI = "Tải trang thất bại, có thể proxy không khả dụng"
        self.failOnLoadingPage = "Tải trang thất bại"
        self.IPBlocked = "Tải trang thất bại, địa chỉ IP của máy chủ có thể bị chặn"
        self.seeLog = "Tải trang thất bại, vui lòng kiểm tra nhật ký để biết chi tiết"
        self.failOnGettingCaptcha = "Không thể lấy được captcha"
        self.failOnRetrievingPage = "Không thể lấy nội dung trang, đang thoát khỏi chương trình"
        self.proxyEnabledGettingContent = "Không thể lấy nội dung trang, có thể proxy không khả dụng"
        self.failOnGettingPage = "Không thể lấy nội dung trang"
        self.captchaCorrect = "Captcha chính xác"
        self.captchaFail = "Captcha không chính xác, vui lòng thử lại"
        self.login = "Đăng nhập thành công"
        self.loginFail = "Đăng nhập thất bại"
        self.blocked = "Không thể xử lý yêu cầu, tài khoản có thể không hợp lệ hoặc địa chỉ IP của máy chủ có thể bị chặn"
        self.loginFailCheckLog = "Login failed, account may be invalid or server IP may be blocked, " \
                                 "please check the backend log for details"        
        self.notLocked = "Tài khoản không bị khóa"
        self.locked = "Tài khoản bị khóa"
        self.twoStepnotEnabled = "2FA không được kích hoạt"
        self.twoStepEnabled = "2FA đã được kích hoạt"
        self.cantFindDisable2FA = "Không thể tắt 2FA, tài khoản có thể không cho phép tắt 2FA"
        self.rejectedByApple = "Hành động bị từ chối bởi Apple, có nghi ngờ về rủi ro"
        self.chooseFail = "Không thể chọn tùy chọn, không thể mở khóa bằng câu hỏi bảo mật"
        self.loginLoadFail = "Tải trang đăng nhập thất bại"
        self.answerIncorrect = "Câu trả lời cho câu hỏi bảo mật không chính xác, chương trình đã thoát"
        self.answerNotMatch = "Không tìm thấy câu trả lời cho câu hỏi bảo mật, vui lòng kiểm tra cấu hình"
        self.failOnBypass2FA = "Bỏ qua 2FA thất bại"
        self.startRemoving = "Bắt đầu xóa thiết bị"
        self.noRemoveRequired = "Không có thiết bị để xóa"
        self.finishRemoving = "Hoàn thành xóa thiết bị"
        self.DOB_Error = "Không thể lấy câu hỏi bảo mật, ngày sinh có thể không chính xác"
        self.failOnAnswer = "Câu trả lời cho câu hỏi bảo mật không chính xác"
        self.passwordNotFound = "Không tìm thấy hộp mật khẩu"
        self.unknownError = "Đã xảy ra lỗi không xác định khi thực hiện nhiệm vụ"
        self.passwordUpdated = "Mật khẩu đã được cập nhật, mật khẩu mới là "
        self.startChangePassword = "Bắt đầu thay đổi mật khẩu"
        self.failOnChangePassword = "Không thể thay đổi mật khẩu ngay bây giờ, có thể 2FA không được tắt"
        self.failToUseSecurityQuestion = "Không thể sử dụng câu hỏi bảo mật để đặt lại mật khẩu, thay đổi mật khẩu thất bại"
        self.TGFail = "Gửi tin nhắn Telegram thất bại"
        self.cnTG = "Nếu máy chủ của bạn ở Trung Quốc đại lục, vui lòng không kích hoạt thông báo Telegram"
        self.failOnCallingWD = "Gọi Webdriver thất bại"
        self.twoStepDetected = "2FA đã được kích hoạt, bắt đầu mở khóa"
        self.accountLocked = "Tài khoản bị khóa, bắt đầu mở khóa"
        self.updateSuccess = "Cập nhật tài khoản thành công"
        self.newPassword = "Mật khẩu mới: "
        self.passwordChanged = "Mật khẩu không chính xác, bắt đầu thay đổi mật khẩu"
        self.LoginFail = "Đăng nhập Apple ID thất bại, không thể xóa thiết bị"
        self.missionFailed = "Nhiệm vụ thất bại, đang chờ kiểm tra tiếp theo"
        self.WDCloseError = "Đóng Webdriver thất bại"
        self.repoAddress = "Địa chỉ repo dự án"
        self.TG_Group = "Nhóm Telegram"
        self.version = "Phiên bản hiện tại"
        self.UnlockFail = "Mở khóa thất bại"
        self.FailToChangePassword = "Thay đổi mật khẩu thất bại"
        self.CurrentAccount = "Tài khoản hiện tại:"
        self.invalidProxyType = "Loại proxy không hợp lệ"
        self.failOnSavingScreenshot = "Không thể lưu ảnh chụp màn hình của trang lỗi"
        self.screenshotSaved = "Screenshot of error page saved to /app/error.html and /app/error.png, " \
                               "please contact the developer"        
        self.getIPFail = "Không thể lấy địa chỉ IP hiện tại"
        self.updateFail = "Cập nhật tài khoản thất bại"
        self.getAPIFail = "Lấy cấu hình từ API thất bại"
        self.checkComplete = "Kiểm tra tài khoản hoàn tất"


    def nextRun(self, time):
        return f"Next job will be executed in {time} minutes"

    def totalDevices(self, total):
        return f"{total} devices in total"
