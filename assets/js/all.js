// 畫面捲動時 navbar logo 縮小
$(function(){
	$(window).scroll(function(){
		if($(window).scrollTop() > 40){
      $('.navbar-brand .navbar-brand-img-center').css('width', '100px');
		} else {
      $('.navbar-brand .navbar-brand-img-center').css('width', '200px');
    }
    });
});

// popover
// $(function () {
//     $('[data-toggle="popover"]').popover();
// });


// emailjs
$("#surveySubmitId").click(function(){
    var surveyUserNameId = $("#surveyUserNameId").text();
    var surveyServiceId = $("#surveyServiceId").text();
    console.log(surveyUserNameId, surveyServiceId);
});
/*
function sendSurvey() {
    let template_params = {
        "userMail": "shooboost@gmail.com",
        "user": "麻糬麻糬",
    };
    emailjs.init("user_YM7dUJypL1Oog3Z6A0Clp");

    var service_id = "default_service";
    var template_id = "wedding_2020";
    emailjs.send(service_id, template_id, template_params);
    console.log("emailjs send")
}*/
// const submitBtn = document.querySelector('[data-action="submit"]');
const submitBtn = document.getElementById('surveySubmitId');

submitBtn.addEventListener("click", processFormData);

    function processFormData(e) {
        // 服務需求
        const services = document.getElementsByName('services');
        const selectedServices = [];
        // 婚禮形式
        const type = document.getElementsByName('surveyTypeId');
        const selectedType =[];
        //餐點形式
        const mealForm = document.getElementsByName('mealForm');
        const mealFormList = []
        //宴客時間
        const banquetTime = document.getElementsByName('banquetTime');
        const banquetTimeList = []

        //雙語服務
        const bilingual = document.getElementsByName('bilingual');
        const bilingualList=[]
        //喜帖設計
        const stickerDesign = document.getElementsByName('stickerDesign');
        const stickerDesignList=[]

        //如何得知我們
        const surveyUserSourceId = document.getElementsByName('surveyUserSourceId');
        const surveyUserSourceList =[];
        
        for (let i = 0; i < services.length; i++) {
          if (services[i].checked) {
            selectedServices.push(services[i].value);
          }
        }
        for (let i = 0; i < type.length; i++) {
            if (type[i].checked) {
                selectedType.push(type[i].value);
            }
          }
          //如何得知
        for (let i = 0; i < surveyUserSourceId.length; i++) {
            if (surveyUserSourceId[i].checked) {
                surveyUserSourceList.push(surveyUserSourceId[i].value);
            }
          }
        for (let i = 0; i < stickerDesign.length; i++) {
            if (stickerDesign[i].checked) {
                stickerDesignList.push(stickerDesign[i].value);
            }
          } 

        for (let i = 0; i < bilingual.length; i++) {
            if (bilingual[i].checked) {
                bilingualList.push(bilingual[i].value);
            }
          }  
        for (let i = 0; i < mealForm.length; i++) {
            if (mealForm[i].checked) {
                mealFormList.push(mealForm[i].value);
            }
          } 
          for (let i = 0; i < banquetTime.length; i++) {
            if (banquetTime[i].checked) {
                banquetTimeList.push(banquetTime[i].value);
            }
          }     
        e.preventDefault();
        //取得 name 屬性為 form 的表單
        const form = document.forms['form'];
        //取 elements 集合中 name 屬性為 name 的值
        const UserName = form.elements.surveyUserNameId.value;
        const UserEmail = form.elements.surveyUserEmailId.value;
        const UserLine = form.elements.surveyUserLineId.value;
        const UserPhone = form.elements.surveyUserPhoneId.value;
        // const Service = form.elements.surveyServiceId.value;
        const Service = selectedServices;
        const Date = form.elements.surveyDateId.value;
        // const Type = form.elements.surveyTypeId.value;
        const Scenes = form.elements.surveyScenesId.value;
        // const Location = form.elements.surveyLocationId.value;
        // const UserVenue = form.elements.surveyUserVenueId.value;
        const Attendance = form.elements.surveyAttendanceId.value;
        // const ChineseCeremony = form.elements.surveyChineseCeremonyId.value;
        // const Bilingual = form.elements.surveyBilingualId.value;
        // 服務需求
        const Type = selectedType;        
        //餐點形式
        const MealFormList = mealFormList
        let mealFormOtherInput = form.elements.mealFormOtherInput.value;
        if(mealFormOtherInput.length > 0 ){
            MealFormList.push(mealFormOtherInput)
         }
        //雙語服務
        const Bilingual = bilingualList;
        //喜帖設計 
        // const InvitationCard = form.elements.surveyInvitationCardId.value;
        const InvitationCard = stickerDesignList;
        // const UserSource = form.elements.surveyUserSourceId.value;
       //如何得知
       let otherSurveyUserSourceIdInput = form.elements.surveyUserSourceIdInput.value;
       let surveyUserSourceMRIdInput =form.elements.surveyUserSourceMRIdInput.value;
       if(otherSurveyUserSourceIdInput.length > 0 ){
           surveyUserSourceList.push(otherSurveyUserSourceIdInput)
        }
        if(surveyUserSourceMRIdInput.length > 0 ){
            surveyUserSourceList.push(surveyUserSourceMRIdInput)
         }
 


        const UserSource = surveyUserSourceList;
        const Progress = form.elements.surveyProgressId.value;
        const Submit = form.elements.surveySubmitId.value;
       
        let template_params = {
            "UserName": UserName,
            "UserEmail": UserEmail,
            "UserPhone": UserPhone,
            "Service": Service,
            "Date": Date,
            "Type": Type,
            "Scenes": Scenes,
            // "Location": Location,
            // "UserVenue": UserVenue,
            "Attendance": Attendance,
            // "ChineseCeremony": ChineseCeremony,
            "Bilingual": Bilingual,
            "InvitationCard": InvitationCard,
            "UserSource": UserSource,
            "Progress": Progress,
            "Line":UserLine,
            "Submit": Submit,
            "MealFormList":MealFormList
        };
         let mustCheck_params = {
            "UserName": UserName,
            "UserEmail": UserEmail,
            "UserPhone": UserPhone,
            "Date": Date,
            "Scenes":Scenes,
            "Attendance":Attendance,
         }
        console.log(template_params ,'template_params')
        for (let key in mustCheck_params) {
            if (mustCheck_params[key] === "") {
                console.log(`Key: ${key} has empty value.`);
                return
            }
          }  

        // 要使用再打開 yooo
        /**/
        // emailjs.init("user_YM7dUJypL1Oog3Z6A0Clp");
        // var service_id = "default_service";
        // var template_id = "wedding_2020";
        // emailjs.send(service_id, template_id, template_params);
        //公鑰
        
        emailjs.init("GW5fMt_RXRxjeBdT9");
        var service_id = "service_x0pe893";
        var template_id = "template_2nbvo2s";
        emailjs.send(service_id, template_id, template_params);
        console.log("emailjs send");
        alert("成功寄出預約表單囉")
        
}
















