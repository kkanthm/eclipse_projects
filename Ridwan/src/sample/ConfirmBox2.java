package sample;
import java.lang.*;
import javafx.stage.*;
import javafx.scene.layout.*;
import javafx.geometry.*;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import ques11.src.com.company.Ques11;
import ques12.src.com.company.Ques12;
import ques15.src.com.company.Ques15;
import ques16.src.com.company.Ques16;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import java.lang.String;
import java.lang.*;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.*;

public class ConfirmBox2{
    //Create variable
    static boolean answer;
  //  static  RadioButton correctOption ;
    static int count;
    static int rightans;
  //  static ArrayList answersList;


    //    public  void setQuestion( String Question) {
//	question = new Label();
//	question.setText(Question);
//	System.out.println("A");
//	}
//    public Label getQuestion() {
//    	return this.question;
//    }
    static String result;
    //static VBox radios;

    //    public  void setQuestion( String Ques) {
//    	this.Question = Ques;
//    }
//    public String getQuestion() {
//    	return this.Question;
//    }
    public static String Randomise()
    {
        int a,b;
        Random rand = new Random();
        a = rand.nextInt(5 + 1 - (-5)) + (-5);
        b = rand.nextInt(5 + 1 - (-5)) + (-5);
        String stra = Integer.toString(a);
        String strb = Integer.toString(b);
        String val= stra+"+"+strb+"i";
        return val;
    }
    public static void setSceneAndShow( Stage window) {
        window.show();
    }

    public static void display(String nameInput, String passLabel, Stage window) {


        String name, grade;
        name="Name: ";
        grade="Grade: ";

        String nameIn=name+nameInput;
        String gradeIn=grade+passLabel;

        window.initModality(Modality.APPLICATION_MODAL);
        window.setTitle("SAT Practice Demo");
        window.setMinWidth(1080);

        Label label = new Label();
        label.setText(gradeIn);

        //GridPane with 10px padding around edge
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(10, 10, 10, 10));
        grid.setVgap(8);
        grid.setHgap(10);

        Label nameLabel=new Label(nameIn);
        nameLabel.setId("boldLabel");
        GridPane.setConstraints(nameLabel, 0, 0);


        Label passInput = new Label(gradeIn);
        passInput.setId("boldLabel");
        GridPane.setConstraints(passInput, 0, 1);

        //Create two buttons
        Button yesButton = new Button("Next ");
        yesButton.getStyleClass().add("buttonBlue");
        GridPane.setConstraints(yesButton, 80, 0);
        Button noButton = new Button("End exam");
        GridPane.setConstraints(noButton, 81, 0);
        //Clicking will set answer and close window


        VBox layout = new VBox();
        layout.setPrefWidth(300);
        layout.setSpacing(20);
        layout.setPadding(new Insets(15,15,15,15));

        VBox radios = new VBox();
        radios.setPrefWidth(300);
        radios.setSpacing(20);
        radios.setPadding(new Insets(15,15,15,15));

        Label questionLabel = new Label();
        questionLabel.setText(Ques1.getQues());

        result = Ques1.getResult();

        //Create togglegroup
        ToggleGroup answer1=new ToggleGroup();
        RadioButton a=new RadioButton();
        a.setToggleGroup(answer1);
        a.getStyleClass().add("label");
        RadioButton b=new RadioButton();
        b.setToggleGroup(answer1);
        b.getStyleClass().add("label");
        RadioButton c=new RadioButton();
        c.setToggleGroup(answer1);
        c.getStyleClass().add("label");
        RadioButton d=new RadioButton();
        d.setToggleGroup(answer1);
        d.getStyleClass().add("label");
        RadioButton e=new RadioButton();
        e.setToggleGroup(answer1);
        e.getStyleClass().add("label");
        GridPane.setConstraints(radios, 50, 22);
        //layout.getChildren().addAll(radios,question,answer1);
        //GridPane.setConstraints(no, 50, 47);

        // Scene scene1  = new

        List<RadioButton> givenList = Arrays.asList(a,b,c,d,e); // new ArrayList<RadioButton>();
        Random rand1 = new Random();
        RadioButton randomOption = givenList.get(rand1.nextInt(givenList.size()));
        for (RadioButton bu: givenList) {
            if(bu.equals(randomOption)) {
                bu.setText(result);
                //correctOption = bu;
   // answersList.add(bu);
            }
            else {
                bu.setText(Randomise());
            }
        }
        List<RadioButton> givenList1 = Arrays.asList(a,b,c,d,e);
        for (RadioButton button1 : givenList1) {

            if(button1.equals(randomOption)) {
                button1.setOnAction(event -> {
                    if(button1.isSelected())
                    {
                        System.out.println("\nCorrect Answer!!!");
                        rightans++;
                    }
                });
            }

        }


        yesButton.setOnAction(event -> {
            count++;

            if(count==1) {

                questionLabel.setText(Ques2.getQuestion());
                System.out.println(questionLabel.getText());
                result = Ques2.getResult();

                Random rand2 = new Random();
                RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                for (RadioButton bu: givenList) {
                    if(bu.equals(randomOption1)) {
                        bu.setText(result);
                       // correctOption = bu;
                       // answersList.add(bu);
                    }
                    else {
                        bu.setText(Ques2.getOption());
                    }


                }
                for (RadioButton button : givenList) {

                    if(button.equals(randomOption1)) {
                        button.setOnAction(ev -> {
                            if(button.isSelected())
                            {
                                System.out.println("\nCorrect Answer!!!");
                                rightans++;
                            }
                        });
                    }

                }



            }

            if(count==2) {

                questionLabel.setText(Ques3.getQuestion());
                System.out.println(questionLabel.getText());
                result = Ques3.getResult();

                Random rand2 = new Random();
                RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                for (RadioButton bu: givenList) {
                    if(bu.equals(randomOption1)) {
                        bu.setText(result);
                       // correctOption = bu;
                       // answersList.add(bu);
                    }
                    else {
                        bu.setText(Ques3.getOption());
                    }
                /*    if(bu.getText().equals(result) && bu.isSelected()){
                        System.out.println("Right answe ++");
                        rightans++;
*/

                }
//                if(correctOption.isSelected()){
//                    rightans++;
//                    System.out.println("Right Incremented "+rightans);
//                }
//                else{
//                    System.out.println("Wrong and right ans "+result);
//                }



            }

            if(count==3) {

                questionLabel.setText(Ques4.getQuestion());
                System.out.println(questionLabel.getText());
                result = Ques4.getResult();

                a.setText(Ques4.getResult());
                b.setText("Kathy will complete the repairs within 108 days.");
                c.setText("Kathy repairs phones at the rate of 108 per hour");
                d.setText("Kathy repairs phones at the rate of 108 per hour");
                e.setText("Kathy repairs 108 phones every 6 months");
//                correctOption = a;
//                if(correctOption.isSelected()){
//                    rightans++;
//                    System.out.println("Right Incremented "+rightans);
//                }
//                else{
//                    System.out.println("Wrong and right answer is "+result);
//                }


            }



            if(count==4) {
                questionLabel.setText(Ques5.getQuestion());
                System.out.println(questionLabel.getText());
                result = Ques5.getResult();

                Random rand2 = new Random();
                RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                for (RadioButton bu : givenList) {
                    if (bu.equals(randomOption1)) {
                        bu.setText(result);
//                        correctOption = bu;
                    } else {
                        bu.setText(Ques5.getOption());
                    }
                   /* if(bu.getText().equals(result) && bu.isSelected()){
                        System.out.println("Right answe ++");
                        rightans++;
                    }*/

                }
//                if(correctOption.isSelected()){
//                    rightans++;
//                    System.out.println("Right Incremented "+rightans);
//                }
//                else{
//                    System.out.println("Wrong");
//                }
//                System.out.println(result);
//            }

                if (count == 5) {
                    questionLabel.setText(Ques6.getQuestion());
                    System.out.println(questionLabel.getText());
                    result = Ques6.getResult();
                    Random rand2 = new Random();
                    RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                    for (RadioButton bu : givenList) {
                        if (bu.equals(randomOption1)) {
                            bu.setText(result);
                            //  correctOption = bu;
                        } else {
                            bu.setText(Ques6.getOption());
                        }

                    }

                }

                if (count == 10) {

                    // cbox.setQuestion( Ques11.getQuestion());
                    // System.out.println(cbox.getQuestion().getText()+"\n");

                    questionLabel.setText(Ques11.getQuestion());
                    System.out.println(questionLabel.getText());
                    result = Ques11.getResult();

                    Random rand2 = new Random();
                    RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                    for (RadioButton bu : givenList) {
                        if (bu.equals(randomOption1)) {
                            bu.setText(result);
                        } else {
                            bu.setText(Ques11.getOption());
                        }
                    }

                }
                if (count == 11) {
                    questionLabel.setText(Ques12.getQuestion());
                    System.out.println(questionLabel.getText());
                    result = Ques12.getResult();

                    Random rand2 = new Random();
                    RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                    for (RadioButton bu : givenList) {
                        if (bu.equals(randomOption1)) {
                            bu.setText(result);
                            // correctOption = bu;
                        } else {
                            bu.setText(Ques12.getOption());
                        }
                    }
                    //

                }

                if (count == 14) {
                    questionLabel.setText(Ques15.getQuestion());
                    System.out.println(questionLabel.getText());
                    result = Ques15.getResult();

                    Random rand2 = new Random();
                    RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                    for (RadioButton bu : givenList) {
                        if (bu.equals(randomOption1)) {
                            bu.setText(result);
                            // correctOption = bu;
                        } else {
                            bu.setText(Ques15.getOption());
                        }
                    }


                }

                if (count == 15) {
                    questionLabel.setText(Ques16.getQuestion());
                    System.out.println(questionLabel.getText());
                    result = Ques16.getResult();

                    Random rand2 = new Random();
                    RadioButton randomOption1 = givenList.get(rand2.nextInt(givenList.size()));
                    for (RadioButton bu : givenList) {
                        if (bu.equals(randomOption1)) {
                            bu.setText(result);
                            // correctOption = bu;
                        } else {
                            bu.setText(Ques16.getOption());
                        }
                    }

                }

                )};


        GridPane.setConstraints(questionLabel, 50, 20);
        Button submit =new Button("Submit");
        submit.getStyleClass().add("buttonBlue");
        GridPane.setConstraints(submit, 50, 25);

        System.out.println(questionLabel.getText()+"\n");

//        if(correctOption.isSelected()){
//            rightans++;
//            System.out.println("Right Incremented "+rightans);
//        }
//        else{
//            System.out.println("Wrong"+rightans);
//        }

        noButton.setOnAction(event -> {

            Stage window2 = new Stage();
            window2.setTitle("SAT Practice Demo");
            GridPane grid2 = new GridPane();
            grid2.setPadding(new Insets(10, 10, 10, 10));
            grid2.setVgap(8);
            grid2.setHgap(10);

            //Name Label - constrains use (child, column, row)
            Label RightLabel = new Label("Right answers:         ");
            GridPane.setConstraints(RightLabel, 0, 0);
            Label WrongLabel = new Label("Wrong answers:         ");
            GridPane.setConstraints(WrongLabel, 0, 2);

            grid.getChildren().addAll(RightLabel, WrongLabel);

            Scene scene = new Scene(grid, 300, 200);
            scene.getStylesheets().add("viper.css");
            window2.setScene(scene);
            window2.show();

        });

        radios.getChildren().addAll(a,b,c,d,e);
        grid.getChildren().addAll(nameLabel, passInput, radios, questionLabel,submit, yesButton, noButton);
        Scene scene = new Scene(grid, 1350, 700);
        scene.getStylesheets().add("viper.css");
        window.setScene(scene);
        //window.show();

        //Make sure to return answer
        setSceneAndShow(window);
    }

}